# users/urls.py
from django.urls import path
from .views import signup, log_in, log_out
from. import views
urlpatterns = [
        path('register/',views.register),
        path('login/',views.LoginView.as_view()),
        path('get-otp/<str:email>',views.get_otp),
        path('verify-otp/',views.verify_otp),
    # path('signup/', signup, name='signup'),
    # path('login/', log_in, name='login'),
    # path('logout/', log_out, name='logout'),
]