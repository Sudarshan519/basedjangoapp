from django.urls import path 
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register(r'sites', views.SiteViewSet)
urlpatterns = [
        path('site-detail/', views.sitedetail),
    # path('signup/', signup, name='signup'), 
]

urlpatterns += router.urls