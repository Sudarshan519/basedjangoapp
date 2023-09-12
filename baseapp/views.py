from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from . models import Contact,CurrencyRate
from . serializer import ContactSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from rest_framework import generics
# Create your views here.
def index(request): 
    contactlist=Contact.objects.all()[:100]
    return render(request,'admin/index.html',{"contacts":contactlist})
    return render(request,'baseapp/index.html',{"contacts":contactlist})

@csrf_exempt
def contactSubmit(request):
    i=0
    contactlist=[]
    # while i<10000:
        # i+=1
    contact=Contact()
    contact.email=request.POST['email']
    contact.message=(request.POST['message'])
    contact.save()
    contactlist.append(contact)    
        # contactlist=Contact.objects.all().order_by('-id')[:10]
    # Contact.objects.bulk_create(contactlist)
    # 
    # return redirect("index", )
# {"message":"Your message have been saved successfully"}
    return render(request,'baseapp/base.html',{"contacts":contactlist,"message":"Your message have been saved successfully"})
# @cache_page(60 * 15, cache="special_cache")
class AllContacts(generics.ListAPIView):
        queryset=Contact.objects.all()#[:100]
        serializer_class = ContactSerializer
    # def get(self,request, format=None):
    #     serializer=ContactSerializer(contact,many=True)
    #     return Response(serializer.data)


from . exchange_rates import get_rates
@api_view(['GET'])
def get_rates_list(request):
    data=(get_rates())
    objects=[]
    for kv in (data['data']['payload']):
        # print(kv)
        # print(data[kv])
        created_at=kv['published_on']
        # print(created_at)
        updated_at=kv['modified_on']
        for a in kv['rates']:
            # print(a)
            currencyrate=CurrencyRate()
            # currencyrate.created_at=created_at
            # currencyrate.updated_at=updated_at
            
            currencyrate.name=a['currency']['name']
            currencyrate.iso3=a['currency']['iso3']
            currencyrate.buy=a['buy']
            currencyrate.sell=a['sell']
            currencyrate.unit=a['currency']['unit']
            # print(currencyrate)
            # currencyrate.save()
            objects.append(currencyrate)

        # print(len(objects))
        CurrencyRate.objects.bulk_create(objects)
        # print(data[kv])
        # for k,v in data[kv]:
        #     print(k)
        #     print(v)

        # print(v)

    return JsonResponse({"exchange_rates":data}) #json.loads(data)})

def portfolio(request):
    return render(request,'index.html', )