from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . models import Contacts


# Create your views here.
def index(request):
    return render(request,'baseapp/index.html')

@csrf_exempt
def contactSubmit(request):
    contact=Contacts()
    contact.email=request.POST['email']
    contact.message=(request.POST['message'])
    contact.save()
    return render(request,'baseapp/index.html',{"message":"Your message have been saved successfully"})