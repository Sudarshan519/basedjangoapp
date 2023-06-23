from django.contrib import admin
from .models import Banner
# Register your models here.
class BannersAdmin(admin.ModelAdmin): # new
    readonly_fields = ['img_preview']
    list_display = ['url', 'img_preview']
admin.site.register(Banner,BannersAdmin)