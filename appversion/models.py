from django.db import models

# Create your models here.
class IOSVersion(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    version=models.IntegerField(verbose_name='Version')
    build_number=models.IntegerField(verbose_name='Build Number')
    action=models.CharField(choices=("ForceUpdate","NoAction","SoftUpdate","UnderMaintainence"))
    title=models.CharField(max_length=256,blank=True,null=True)
    desc=models.CharField(max_length=256,blank=True,null=True)
    
class AndroidVersion(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    version=models.IntegerField(verbose_name='Version')
    build_number=models.IntegerField(verbose_name='Build Number')
    action=models.CharField(choices=("ForceUpdate","NoAction","SoftUpdate","UnderMaintainence"))
    title=models.CharField(max_length=256,blank=True,null=True)
    desc=models.CharField(max_length=256,blank=True,null=True)