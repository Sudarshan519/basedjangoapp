from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Banner(models.Model):
    title=models.CharField(max_length=256,null=True,blank=True)
    logo=models.ImageField(_("Banner Image"), upload_to='media/', height_field=None, width_field=None, max_length=None,null=True,blank=True)
    url=models.CharField(max_length=256)
    def img_preview(self): #new
        return mark_safe('<img src = "{url}" height = "80" width="140"/>'.format(
             url = self.logo.url
         ))

