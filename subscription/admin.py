from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Subscription)
admin.site.register(Plan)
admin.site.register(Payment)
admin.site.register(SubscriptionFeature)
# admin.site.register(Plan)
