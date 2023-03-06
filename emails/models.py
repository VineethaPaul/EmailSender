from django.db import models

class EmailScheduler(models.Model):
    id_email        =   models.AutoField(primary_key=True)
    toAddress       =   models.CharField(max_length=1000,blank=True, null=True)
    subject         =   models.CharField(max_length=1000,blank=True, null=True)
    message         =   models.CharField(max_length=5000,blank=True, null=True)
    files           =   models.FileField(upload_to='emailFiles/', blank=True, null=True)
    forEvery        =   models.CharField(max_length=500,null=True,blank=True)
    scheduledTime   =   models.CharField(max_length=500,null=True,blank=True)
    createdAt       =   models.DateTimeField(auto_now_add=True,null=True, blank=True)
    createdBy       =   models.CharField(max_length=500,null=True, blank=True)

    class Meta:
        managed     =   False
        db_table    =   'emailScheduler'