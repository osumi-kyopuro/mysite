from django import forms
from .models import Attendance
class AttendForm(forms.ModelForm):

    class Meta:
        model = Attendance
        fields = ('user', 'scheduled_attend_time', 'scheduled_leave_time',  'attend_time', 'leave_time',
        'remarks')
        labels = {
            'user': 'スタッフ情報',
            'scheduled_attend_time': '出勤予定時間',
            'scheduled_leave_time': '退勤予定時間',
            'attend_time': '出勤時間',
            'leave_time': '退勤時間',
            'remarks': '備考欄'
        }
        help_texts = {
            'user': 'スタッフ情報を入力(必須)',
            'scheduled_attend_time': '出勤予定時間を入力(必須)',
            'scheduled_leave_time': '退勤予定時間を入力(必須)',
            'attend_time': '出勤時間を入力(任意)',
            'leave_time': '退勤時間を入力(任意)',
            'remarks': '備考欄を入力(任意)'
        }