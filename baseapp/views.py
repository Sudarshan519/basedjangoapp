from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from . models import Contacts


# Create your views here.
def index(request):
    contactlist=Contacts.objects.all()

    return render(request,'baseapp/index.html',{"contacts":contactlist})

@csrf_exempt
def contactSubmit(request):
    contact=Contacts()
    contact.email=request.POST['email']
    contact.message=(request.POST['message'])
    contact.save()
    contactlist=Contacts.objects.all()

    # 
    # return redirect("index", )
# {"message":"Your message have been saved successfully"}
    return render(request,'baseapp/index.html',{"contacts":contactlist,"message":"Your message have been saved successfully"})