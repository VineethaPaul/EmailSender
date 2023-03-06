from django.core.mail import EmailMessage
from django.conf import settings

def sendEmailFunc(emailSubject,messageBody,toAddress,attachedFiles):
    sendMail = EmailMessage(
                emailSubject,
                messageBody,
                settings.EMAIL_HOST_USER,
                toAddress,
            )

    for f in attachedFiles:
        sendMail.attach(f.name, f.read(), f.content_type)
    print(sendMail,'sendMailsendMail')
    sendMail.send()
    return 'Mail Sent Successfully'