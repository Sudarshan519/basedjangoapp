from django.urls import path
from . import views

urlpatterns = [
    path('subscribe/<int:plan_id>/', views.subscribe, name='subscribe'),
    path('profile/', views.profile, name='profile'),
    #    path('register/', views.register, name='register'),
    # path('login/', views.user_login, name='login'),
    # path('logout/', views.user_logout, name='logout'),
]