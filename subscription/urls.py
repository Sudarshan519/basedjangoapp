from django.urls import include, path
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'plans',views.PlanViewSet,basename='plans')
router.register(r'subscription',views.SubscriptionViewSet,basename='subscription')
urlpatterns = [
     path('', include(router.urls)),
    path('subscribe/<int:plan_id>/', views.subscribe, name='subscribe'),
    path('profile/', views.profile, name='profile'),
    # path('plans/',view=views.PlanViewSet),
    # path('subscription/',views=views.SubscriptionViewSet)
    #    path('register/', views.register, name='register'),
    # path('login/', views.user_login, name='login'),
    # path('logout/', views.user_logout, name='logout'),
]