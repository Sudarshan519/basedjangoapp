from django.contrib import admin

from website.models import SiteSettingsData, StepsToStartUp, TermsAndConditions, WhatYouCanDo, WhyChooseUs

# Register your models here.
admin.site.register(SiteSettingsData)
admin.site.register(WhyChooseUs)
admin.site.register(StepsToStartUp)
admin.site.register(WhatYouCanDo)
admin.site.register(TermsAndConditions)