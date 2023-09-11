from django.contrib import admin
from django.urls import path,include,re_path
from django.views.decorators.cache import cache_page

from . import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      urlpath='hajir.urls',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
urlpatterns = [ 
               re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('',views.portfolio,name="index"),
    path('contact/',views.contactSubmit),
    path('api/v1/contacts/',  (views.AllContacts.as_view())),
    path('get_rates_list',views.get_rates_list),
     path('app',views.index),
       path('',include('website.urls')),
       path('',include('streaming_app.urls'))
    # path('api/v1/contacts', cache_page(60 * 15)(views.AllContacts.as_view()))
]
