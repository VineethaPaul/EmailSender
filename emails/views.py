from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

#mail import
from django.core.mail import EmailMessage

from django.conf import settings
# from django.utils import timezone
from .tasks import send_email_task
from django_celery_beat.models import PeriodicTask,CrontabSchedule
import json

# class MyJsonEncoder(DjangoJSONEncoder):
#     def default(self, o):
#         if isinstance(o, InMemoryUploadedFile):
#            return o.read()
#         return str(o)


# from django.forms.models import model_to_dict

# data = self.get_queryset()

# for item in data:
#    item['product'] = model_to_dict(item['product'])

# return HttpResponse(json.simplejson.dumps(data), mimetype="application/json")


import base64

# file_obj = request.FILES['file']
# file_data = base64.b64encode(file_obj.read()).decode('utf-8')


from django.http import JsonResponse


# file_content = file_obj.read()  # Read the content of the file
# file_data = {
#     "file_name": file_obj.name,
#     "file_content": file_content,
# }

# Convert file_data to a JSON string
# json_data = json.dumps(file_data)

def SendEmail(request):
    if request.method == 'POST':
        emailSubject    =   request.POST['emailSubject']
        messageBody     =   request.POST['message']
        attachedFiles   =   request.FILES['attachedFiles']
        scheduledDays   =   request.POST['scheduledDays']
        scheduledTime   =   request.POST['scheduledTime']
        try:
            toAddress   =   request.POST['toAddress'].split(',')
        except:
            toAddress   =   [request.POST['toAddress']]
        file_data = base64.b64encode(attachedFiles.read()).decode('utf-8')
        # f = attachedFiles.read()
        # file_data = {
        #     "file_name": attachedFiles.name,
        #     "file_content": f,
        # }
        print(scheduledDays,scheduledTime,toAddress,'toAddresstoAddress',attachedFiles)
        sT = scheduledTime.split(':')
        # try:
        # crontab(minute='*/10',hour='3,17,22', day_of_week='thu,fri')
        schedule, created = CrontabSchedule.objects.get_or_create(hour=sT[0],minute=sT[1],day_of_week=scheduledDays)
        task = PeriodicTask.objects.create(crontab=schedule,name='schedule_email'+'44',task='emails.tasks.send_email_task',
                                           args=json.dumps([emailSubject,messageBody,toAddress,file_data]))
        returnMessage = messages.success(request,'Mail sent successfully') 
        return render(request,'Emails/sendEmail.html',{'message':'Mail sent successfully'})
        # except:
        #     returnMessage = messages.error(request,'Unable to send email. Please try again later') 
        #     return render(request, 'Emails/sendEmail.html',{'returnMessage':returnMessage})
    return render(request,'Emails/sendEmail.html')


