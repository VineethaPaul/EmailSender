from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

#mail import
from django.core.mail import EmailMessage

from django.conf import settings
# from django.utils import timezone
# from .tasks import send_email_task
# from django_celery_beat.models import PeriodicTask,CrontabSchedule

def SendEmail(request):
    if request.method == 'POST':
        emailSubject    =   request.POST['emailSubject']
        messageBody     =   request.POST['message']
        attachedFiles   =   request.FILES.getlist('attachedFiles')
        scheduledDays   =   request.POST['scheduledDays']
        scheduledTime   =   request.POST['scheduledTime']
        try:
            toAddress   =   request.POST['toAddress'].split(',')
        except:
            toAddress   =   [request.POST['toAddress']]
        print(scheduledDays,scheduledTime,toAddress,'toAddresstoAddress',attachedFiles)
        try:
            sendMail = EmailMessage(
                emailSubject,
                messageBody,
                settings.EMAIL_HOST_USER,
                toAddress,
            )
            for f in attachedFiles:
                sendMail.attach(f.name, f.read(), f.content_type)
            sendMail.send()
            # schedule, created = CrontabSchedule.objects.get_or_create(hour=21,minute=13)
            # task = PeriodicTask.objects.create(crontab=schedule,name='schedule_email'+'5',task='emailattachment.tasks.send_email_task')
            returnMessage = messages.success(request,'Mail sent successfully') 
            return render(request,'Emails/sendEmail.html',{'message':'Mail sent successfully'})
        except:
            returnMessage = messages.error(request,'Unable to send email. Please try again later') 
            return render(request, 'Emails/sendEmail.html',{'returnMessage':returnMessage})
    return render(request,'Emails/sendEmail.html')
