from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from .forms import AttendForm
from builtins import str
from _datetime import timezone
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.db.models import F, Q
from django.conf.locale import ja
#import .models

# Create your views here.
def list_check(request):
    from .models import Attendance
    urlName = reverse('list')
    Attendance.objects.filter(scheduled_attend_time__gt=F('scheduled_leave_time')).delete()
    latest_order = Attendance.objects.latest('id')
    if latest_order.attend_time!=None and latest_order.leave_time!=None:
        latest_order.work_time = latest_order.leave_time - latest_order.attend_time
    latest_order.save()
    c = Attendance.objects.filter(Q(user=latest_order.user), Q(scheduled_attend_time__range=(latest_order.scheduled_attend_time-timedelta(minutes=30),latest_order.scheduled_leave_time+timedelta(minutes=30)))|Q(scheduled_leave_time__range=(latest_order.scheduled_attend_time-timedelta(minutes=30),latest_order.scheduled_leave_time+timedelta(minutes=30)))|Q(scheduled_attend_time__gte=latest_order.scheduled_attend_time,scheduled_leave_time__lte=latest_order.scheduled_leave_time)).count()
    if c >= 1:
        Attendance.objects.latest('id').delete()
    data = Attendance.objects.all()
    params = {'message': 'データ一覧', 'data': data}
    return render(request, 'attendance2/list.html', params)

def new(request):
    from .models import Attendance
    urlName = reverse('new')    
    params = {'message': '', 'form': None}
    if request.method == 'POST':
        form = AttendForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_check')
        else:
            params['message'] = '再入力して下さい'
            params['form'] = form
    else:
        params['form'] = AttendForm()
    return render(request, 'attendance2/new.html', params)


def sortlist(request):
    from .models import Attendance
    from django.db.models import Sum
    urlName=reverse('sortlist')
    data = Attendance.objects.order_by("scheduled_attend_time")
    params = {'message': 'データ一覧', 'data': data}
    return render(request, 'attendance2/sortlist.html', params)
 
 
def list(request):
    from .models import Attendance
    urlName=reverse('list')
    data = Attendance.objects.all()
    params = {'message': 'データ一覧', 'data': data}
    return render(request, 'attendance2/list.html', params)



def mylist(request):
    from .models import Attendance
    from django.db.models import Sum
    urlName = reverse('list')
    
    data = Attendance.objects.filter(user=request.user).order_by("scheduled_attend_time")
    absence_count=Attendance.objects.filter(user=request.user,attend_time=None ,leave_time=None,scheduled_leave_time__lt= datetime.now()).count()
    late_count = Attendance.objects.filter(user=request.user,attend_time__gt = F('scheduled_attend_time')).count()
    early_count = Attendance.objects.filter(user=request.user,leave_time__lt=F('scheduled_leave_time')).count()
    sum = data.aggregate(Sum('work_time'))
    params = {'message': 'データ一覧', 'data': data,'sum':sum,'user':request.user,'absence_count':absence_count,'late_count':late_count,'early_count':early_count}
    return render(request, 'attendance2/mylist.html', params)

def erase(request):
    from .models import Attendance
    urlName = reverse('erase')
    return render(request, 'attendance2/erase_menu.html')

def all_erase(request):
    from .models import Attendance
    urlName = reverse('all_erase')
    Attendance.objects.all().delete()
    return redirect('list')

def sub_erase(request):
    from .models import Attendance
    urlName = reverse('sub_erase')
    if Attendance.objects.count()!=0:
        Attendance.objects.latest('id').delete()
    return redirect('list')
    




def time(request):
    urlName=reverse('time')
    n = datetime.now().strftime('%H:%M:%S')
    n+='<p />'
    n+="<a href='../'>勤怠管理ページへ</a><p />"
    return HttpResponse(n)

def attendance_time(request):
    from .models import Attendance
    urlName = reverse('attendance_time')
    if Attendance.objects.filter(user=request.user, attend_time__isnull=False, leave_time=None).exists():
        c=Attendance.objects.filter(user=request.user, attend_time=None, leave_time=None)
        contexts = {
            'c':c,
        }

    data = get_object_or_404(Attendance, Q(user=request.user), Q(scheduled_attend_time__lt=datetime.now()+timedelta(minutes=30)),Q(scheduled_leave_time__gt=datetime.now()),Q(attend_time=None),Q(leave_time=None))
    contexts = {
        'data':data,
    }
    
    data.attend_time = timezone.now()
    if data.attend_time > data.scheduled_attend_time:
        data.late=True
    data.save()
    #data_is_late = data.is_late()
    x = timezone.now()
    x2 = datetime.now().strftime('%H:%M:%S')
    s = ""
    s += str(request.user)
    s+="さん出勤！！<p />"
    s += x2 + '<p />'
    #s += "出勤予定時間<p />"
    #s+=data.scheduled_attend_time.strftime('%H:%M:%S')+'<p />'
    #if data.is_late()==True:
    #    s += "遅刻<p />"
    #else:
    #    s += "通常<p />"
        
    s += "<a href='../'>勤怠管理ページへ</a><p />"
    data.save()
    return HttpResponse(s)


 

def leave_time(request):
    from .models import Attendance
    data = get_object_or_404(Attendance,Q(user=request.user),Q(leave_time=None),Q(attend_time__isnull=False))
    contexts = {
        'data':data,
    }
    data.leave_time = timezone.now()
    if data.leave_time < data.scheduled_leave_time:
        data.early=True
    data.save()
    #data_is_early = data.is_early()
    urlName = reverse('leave_time')
    y2 = datetime.now().strftime('%H:%M:%S')
    data.work_time=data.leave_time - data.attend_time
    s = ""
    s += str(request.user)
    s+="さん退勤！！<p />"
    s += y2 + '<p />'
    #s += "退勤予定時間<p />"
    #s+=data.scheduled_leave_time.strftime('%H:%M:%S')+'<p />'
    s += "今日の労働時間<p />"
    s += str(data.work_time) + '<p />'
    #f data.is_early()==True:
    #    s += "早退<p />"
    #else:
    #    s += "通常<p />"
    s += "<a href='../'>勤怠管理ページへ</a><p />"
    data.save()
    return HttpResponse(s)

def home(request):
    urlName = reverse('home')
    params = {'message': str(request.user)}
    return render(request, 'attendance2/home.html',params)

