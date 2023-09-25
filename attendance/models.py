from django.db import models

# Create your models here.
class Attendance(models.Model):
    login_time=models.TimeField(auto_now_add=True)
    logout_time=models.TimeField()
    break_duration=models.DurationField(name="Break Duration")
    user=models.ForeignKey("auth.User",null=False,blank=False)
    