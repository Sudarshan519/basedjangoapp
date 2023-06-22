from django.contrib import admin
from . models import Contact
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ['email','message']
    
admin.site.register(Contact,ContactAdmin)

# @admin.register(PostalCode)
# class PostalCodeAdmin(admin.ModelAdmin):
#     list_display=[k.name  for k in PostalCode._meta.fields]
# admin.site.register(CurrencyRate)
# @admin.register(CurrencyRate)
class CurrencyRateAdmin(admin.ModelAdmin):
    # list_display=["name","created_at","updated_at"]
    list_display=[k.name  for k in CurrencyRate._meta.fields]
    # list_display=[k for k in CurrencyRate._meta.get_fields()]
    # list_dispaly=('sell')#(k for k in CurrencyRate._meta.get_fields())
    list_filter = ('name','buy','sell', 'created_at','updated_at',)
    # list_display=['name','buy','sell', 'created_at','updated_at',]
    search_fields = ("name",'iso3')
admin.site.register(CurrencyRate,CurrencyRateAdmin)