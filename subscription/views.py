 

# Create your views here.
from django.shortcuts import render, redirect
from .models import Plan, Subscription
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta

@login_required
def subscribe(request, plan_id):
    plan = Plan.objects.get(pk=plan_id)
    user = request.user
    today = date.today()
    end_date = today + timedelta(days=30)  # For simplicity, assuming monthly subscriptions.
    
    # Create a subscription for the user.
    Subscription.objects.create(user=user, plan=plan, start_date=today, end_date=end_date)
    
    return redirect('profile')

@login_required
def profile(request):
    user = request.user
    subscriptions = Subscription.objects.filter(user=user, active=True)
    return render(request, 'profile.html', {'user': user, 'subscriptions': subscriptions})


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')  # Replace 'profile' with your desired URL
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')  # Replace 'profile' with your desired URL
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout

from rest_framework import viewsets
from .models import *
from .serializers import *
class PlanViewSet(viewsets.ModelViewSet):
    queryset=Plan.objects.all()
    serializer_class=PlanSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    # episode=SubscriptionSerializer(many=True,read_only=True)
    queryset = Subscription.objects.filter()
    serializer_class = SubscriptionSerializer