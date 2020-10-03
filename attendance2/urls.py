from django.urls import path
from . import views
import re
urlpatterns = [
    path('', views.home, name='home'),
    path('time', views.time, name='time'),
    path('attendance_time',views.attendance_time,name='attendance_time'),
    path('leave_time', views.leave_time, name='leave_time'),
    path('new', views.new, name='new'),
    path('list', views.list, name='list'),
    path('mylist', views.mylist, name='mylist'),
    path('sortlist', views.sortlist, name='sortlist'),
    path('erase', views.erase, name='erase'),
    path('all_erase', views.all_erase, name='all_erase'),
    path('sub_erase', views.sub_erase, name='sub_erase'),
    path('list_check', views.list_check, name='list_check'),
]