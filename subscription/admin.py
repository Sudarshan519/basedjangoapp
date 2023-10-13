from django.contrib import admin
from .models import Subscription,Plan,Payment,SubscriptionFeature
# Register your models here.
admin.site.register(Subscription)
admin.site.register(Plan)
admin.site.register(Payment)
admin.site.register(SubscriptionFeature)
# admin.site.register(Plan)
