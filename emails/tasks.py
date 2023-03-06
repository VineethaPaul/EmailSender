from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from EmailSender.celery import app

from celery import shared_task
from .email import sendEmailFunc
from django.conf import settings


# @shared_task(name="send_email_task")
# def send_email_task(subject, message, emails, files):
@app.task
def send_email_task(emailSubject,messageBody,toAddress,attachedFiles):
    print("i am inssdfsdfsdide  i888888  task")
    # emailSubject = 'Test Message'
    # messageBody = 'Test Message body Tets'
    # toAddress = ['informjashvavineethapaul@gmail.com']
    # attachedFiles = []
  
    print(emailSubject,messageBody,toAddress,attachedFiles,'attachedFilesattachedFiles')

    from django.core.mail import send_mail

    
    # email_body = render_to_string('email_message.txt', context)
    # sendMail = EmailMessage(
    #             emailSubject,
    #             email_body,   
    #             settings.EMAIL_HOST_USER,
    #             toAddress,
    #         )
    # for f in attachedFiles:
    #     sendMail.attach(f.name, f.read(), f.content_type)
    # sendMail.send()
    sendEmailFunc(emailSubject,messageBody,toAddress,attachedFiles)
    # print(sendEmailFunc,'sendEmailFuncsendEmailFuncsendEmailFunc')
    return 'Done'



    # send_mail(emailSubject,messageBody,toAddress,files)