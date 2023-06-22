from django.db import models

# Create your models here.
class Contacts(models.Model):
    email = models.CharField(max_length=256,)
    message = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.email