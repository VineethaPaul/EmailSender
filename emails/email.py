from django.core.mail import EmailMessage
from django.conf import settings

def sendEmailFunc(emailSubject,messageBody,toAddress,attachedFiles):
    sendMail = EmailMessage(
                emailSubject,
                messageBody,
                settings.EMAIL_HOST_USER,
                toAddress,
            )

    
    print(sendMail,'sendMailsendMail')
    sendMail.send()
    return 'Mail Sent Successfully'