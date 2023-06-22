from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Contact(models.Model):
    email = models.CharField(max_length=256,)
    message = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.email
    
class CurrencyRate(models.Model):
    created_at=models.DateTimeField(_("Created Date"), auto_now=False, auto_now_add=True,null=True)
    updated_at=models.DateTimeField(_("Updated Date"), auto_now=True, auto_now_add=False,null=True)
    iso3=models.CharField(_("ISO3"), max_length=50)
    name=models.CharField(_("NAME"), max_length=50)
    unit=models.IntegerField(_("Unit"),default=1)
    buy=models.FloatField(_("Buy"))
    sell=models.FloatField(_("Sell"))
    # def __str__(self):
    #     return f'{self.name} {self.created_at} {self.updated_at} {self.name} {self.buy} {self.sell}'
    