import base64
import datetime
from django.shortcuts import redirect, render
from django.urls import reverse
from pyotp import HOTP
from userr.models import CustomUser

from userr.serializers import LoginSerializer, RegisterSerializer, VerifyOtpSerializer

# Create your views here.
from .forms import SignUpForm, LogInForm
from django.contrib.auth import authenticate,login,logout
# This class returns the string needed to generate the key
class generateKey:
    @staticmethod
    def returnValue(phone): 
        return str(phone) + str(datetime.date.today()) + "Some Random Secret Key"

def otp_from_email(email):
    keygen = generateKey()
    key = base64.b32encode(keygen.returnValue(email).encode())  # Key is generated
    return HOTP(key) 
def verifyotp(email,otp,counter):
    keygen = generateKey()
    key = base64.b32encode(keygen.returnValue(email).encode())  # Key is generated
    OTP = HOTP(key)
    
    return (OTP.verify(otp,counter))
def fetchToken(user):
    try:
        refresh = RefreshToken.for_user(user)
    
        return  ({
            # "user":user.__dict__,
            # "cuser":model_to_dict(user),
            # "model":model_to_dict(user),
            "email":user.email,
            
            # "isEmailVerified":user.emailVerified,
            "access_token":str(refresh.access_token),
            "refresh_token":str(refresh),
            # "profile_updated":user.profile_updated
        })
    except Exception as e :
        return  str(e)
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()   
    return render(request, 'users/signup.html', {'form': form})


def log_in(request):
    error = False
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)  
                return redirect('home')
            else:
                error = True
    else:
        form = LogInForm()

    return render(request, 'users/login.html', {'form': form, 'error': error})


def log_out(request):
    logout(request)
    return redirect(reverse('users:login'))
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema 
from rest_framework_simplejwt.tokens import RefreshToken
class LoginView(APIView):
    @swagger_auto_schema(tags=['user'], operation_description='otp',request_body=LoginSerializer)
    def post(self, request, refreshformat=None):
        serializer = LoginSerializer(data=request.data,
            context={ 'request': request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        try:
            if(user.email_verified):
                data=fetchToken(user) 
                return Response(data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({"error":"email not verified"})
        except Exception as e:
            return Response(status=400,data={"detail":str(e)})
        
 
        return Response(data, status=status.HTTP_202_ACCEPTED)
    


from rest_framework.decorators import api_view

@swagger_auto_schema(tags=['user'],method='post', operation_description='',request_body=RegisterSerializer)
@api_view(['POST'])
def register(request):
    serializer=RegisterSerializer(data=request.data)
    
    if serializer.is_valid():
        user=serializer.save()
        OTP=otp_from_email(serializer.data['email'])
        # request.headers['email']=serializer.data['email']
        # getPhoneNumberRegistered.get(request),#,email=serializer.data['email'])
        return Response({"otp":OTP.at(user.counter)},status=status.HTTP_201_CREATED)
        getPhoneNumberRegistered.get(email=serializer.data['email'])
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
from django.core.exceptions import ObjectDoesNotExist

@swagger_auto_schema(tags=['user'],method='get', operation_description='')
@api_view(['GET'])
def get_otp(request,email):#email
 
        try:
            user = CustomUser.objects.get(email=email)  # if Mobile already exists the take this else create New One
        except ObjectDoesNotExist:
            return Response({"error":"User not registered"},404)
        OTP=otp_from_email(email)
        counter=user.counter+1
        user.counter=counter
        
        user.save()
        otp=OTP.at(counter)
        verifyotp(email,otp,counter)
        print(counter)
        print(otp)
        # Using Multi-Threading send the OTP Using Messaging Services like Twilio or Fast2sms
        return  Response({"OTP": otp})  # Just for demonstration

@swagger_auto_schema(tags=['user'],method='post', operation_description='',request_body=VerifyOtpSerializer)
@api_view(['POST'])

def verify_otp(request):
    serializer=VerifyOtpSerializer(data=request.data)
    if serializer.is_valid():
        print(serializer.data)
        email=serializer.data['email']
        otp=serializer.data['otp']
    # email=request.data['email']
    # otp=request.data['otp']
    try:
        user=CustomUser.objects.get(email__iexact=email)
        print(user.counter)
        isvalid=verifyotp(email,otp,user.counter)
        user.email_verified=True
        user.save()
        if isvalid:
            return Response({
                "status":True,
                "data":"Email verified"
            })
        return Response({"error":"Otp invalid/expired"})
    except Exception as e:
        return Response({"error":"Otp invalid/expired"+str(e)})
    
    # if(OTP.verify(int(request.data['otp']),user.counter)):
    #             user.emailVerified=True
    #             user.save()
    #             return Response({"success":"Email Verified"})