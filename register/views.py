from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.checks import messages
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from Registration.settings import EMAIL_HOST_USER
from .models import Profile
from django.core.mail import send_mail
from twilio.rest import Client
from django.contrib.auth.hashers import make_password
import math, random
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')
def index(request):
    return render(request, 'landing.html')

def log(request):
    return render(request, 'login.html')

def sign(request):
    return render(request, 'signup.html')



def login_view(request):
    if request.method == 'POST':

        # form = LoginForm(request.POST)
        if request.POST.get('your_name') and request.POST.get('your_pass'):

            username = request.POST['your_name']
            password = request.POST['your_pass']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                if(Profile.objects.filter(user=username,email_confirmed=True,phone_confirmed=True)):
                     return HttpResponseRedirect(reverse('home'))
                else:
                    messages.warning(request, 'Email or Phone is not verified')
                    return HttpResponseRedirect(reverse('log'))
            else:
                messages.warning(request, 'Password  is incorrect ')
                return HttpResponseRedirect(reverse('log'))
        else:
            messages.warning(request, 'Enter a Valid Input')
            return HttpResponseRedirect(reverse('log'))


def otp(request):
    digits = "0123456789"
    OTP = ""

    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


def signup(request):
    if request.method == 'POST':
        print("1")
        if request.POST.get('username') and request.POST.get('F_name') and request.POST.get('L_name') and request.POST.get('email') and request.POST.get('mobile') and request.POST.get('pass') and request.POST.get('repass'):
            print("22")
            v1 = (request.POST['F_name'])
            v2 = (request.POST['L_name'])
            v3 = (request.POST['username'])
            v4 = (request.POST['email'])
            v5 = (request.POST['pass'])
            v6 = (request.POST['repass'])
            v8 = (request.POST['mobile'])
            print("2")
            if v5 == v6:
                if len(v5)>=7:
                    password1=make_password(v5)
                    u=User.objects.filter(username=v3)


                    if not u :
                        v = Profile.objects.filter(email=v4)
                        x = Profile.objects.filter(mobile=v8)

                        if not v:
                            if not x:
                                subject = 'Welcome to DataFlair'
                                message = otp(request)
                                recepient = str(v4)
                                send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)

                                to = '+91' + v8
                                client = Client('ACee71f9f754dee20316564b16bbe51ce6', '491d9fb9cd03700b4db21288d1fe3b62')
                                potp = otp(request)
                                client.messages.create(
                                    body='Your verification otp is ' + potp,
                                    to=to, from_='+12059648218')

                                d = Profile.objects.create(user=v3, first_name=v1, last_name=v2, mobile=v8, email=v4)
                                d.save()
                                E = User.objects.create(username=v3, email=v4, password=password1)
                                E.save()

                                context = {
                                    'username': v3,
                                    'eotp': message,
                                    'potp': potp,
                                }
                                return render(request, 'OTP.html', context)





                            else:
                                messages.warning(request, 'Phone is in Use, Try new ')
                                return HttpResponseRedirect(reverse('sign'))
                        else:
                            messages.warning(request, 'Email is in Use, Try new ')
                            return HttpResponseRedirect(reverse('sign'))

                    else:
                        messages.warning(request, 'Username not available , Try new')
                        return HttpResponseRedirect(reverse('sign'))
                else:
                    messages.warning(request, 'Password  is too small ')
                    return HttpResponseRedirect(reverse('sign'))
            else:

                messages.warning(request, 'Password  not match ')
                return HttpResponseRedirect(reverse('sign'))



def add(request, username, eotp, potp):
        v=eotp
        x=potp
        u=username
        context = {
                      'username':u,
                      'eotp':v,
                         'potp': x,
                    }
        if request.method == 'POST':
            if request.POST.get('email_otp') and request.POST.get('phone_otp'):
                v3 = (request.POST['email_otp'])
                v2 = eotp
                v4 = (request.POST['phone_otp'])
                v5 = potp

                if v3 == v2:
                    messages.warning(request, 'Email account is Verified ')
                    s = Profile.objects.get(user=username)
                    print(s)
                    Profile.objects.filter(user=username).update(email_confirmed=True)
                    if v4 == v5:
                        messages.warning(request, 'Mobile number is Verified ')
                        s = Profile.objects.get(user=username)
                        print(s)
                        Profile.objects.filter(user=username).update(phone_confirmed=True)
                        return render(request, 'login.html', )
                    else:
                        messages.warning(request, 'Phone OTP not match ')
                        return render(request, 'OTP.html', context)

                else:
                    messages.warning(request, 'Email OTP not match ')
                    return render(request, 'OTP.html', context)



