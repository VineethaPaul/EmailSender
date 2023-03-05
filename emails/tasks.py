from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from EmailSender.celery import app

from celery import shared_task
# from django.core.mail import send_email
# from .email import send_email
from django.conf import settings


# @shared_task(name="send_email_task")
# def send_email_task(subject, message, emails, files):
@app.task
def send_email_task():
    print("i am inside task")
    emailSubject = 'Test Message'
    messageBody = 'Test Message body'
    toAddress = ['informjashvavineethapaul@gmail.com']
    attachedFiles = []
    files = ''
    # send_email(emailSubject,messageBody,toAddress,files)
    sendMail = EmailMessage(
                emailSubject,
                messageBody,
                settings.EMAIL_HOST_USER,
                toAddress,
            )
    for f in attachedFiles:
        sendMail.attach(f.name, f.read(), f.content_type)
    sendMail.send()
    return 'Done'


