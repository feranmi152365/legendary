from django.shortcuts import render, redirect
from django.contrib import messages, auth
# from django.contrib.auth.models import User
from .models import CustomUser
from Couponcode.models import Coupon
from Dashboard.models import Refferal
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate


# Create your views here.


def register(request):
    # existingcode = Coupon.objects.get('code')

    # refferal 
    refferal_id = request.session.get('ref_refferal')
    form = request.POST.get('referral')
    # form = CustomUser(request.POST or None)
    if request.method == 'POST':
        # Register User
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']
        username = request.POST['username']
        phoneNumber = request.POST.get('phoneNumber')
        referral = request.POST.get('referral')
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        bankName = request.POST.get('bankName')
        accountName = request.POST.get('accountName')
        accountNumber = request.POST.get('accountNumber')
        coupon = request.POST.get('coupon')
    

        ### password validation
        if password == password2:
            ### Username Validation
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'Username is taken')
                return redirect('register')
            elif CustomUser.objects.filter(email=email).exists():
                messages.success(request, 'Email is taken')
                return redirect('register')
            # elif CustomUser.objects.filter(coupon__in=existingcode).exists():
            #     return redirect('register')
            ### Email Validation
            elif CustomUser.objects.filter(coupon=coupon).exists():
                messages.error(request, 'Coupon is taken')
                return redirect('register')
                # # Email Validation
                # if CustomUser.objects.filter(coupon=coupon).exists():
                #     messages.error(request, 'Coupon is taken')
                #     return redirect('register')

            else:
                if form == form:
                    if refferal_id is not None:
                        recommended_by_refferal = Refferal.objects.get(id=refferal_id)

                        instance= form.save()
                        registered_user = CustomUser.objects.get(id=instance.id)
                        registered_refferal = Refferal.objects.get(user=registered_user)
                        registered_refferal.recommended_by = recommended_by_refferal.user
                        registered_refferal.save()
                    else:
                         user = CustomUser.objects.create_user(username=username, password=password, email=email, last_name=last_name,
                         first_name=first_name,phoneNumber=phoneNumber, referral=referral, bankName=bankName, accountName=accountName,
                         coupon=coupon,accountNumber=accountNumber)

                # else:
                #     user = CustomUser.objects.create_user(username=username, password=password, email=email, last_name=last_name,
                #      first_name=first_name,phoneNumber=phoneNumber, referral=referral, bankName=bankName, accountName=accountName,
                #      coupon=coupon,accountNumber=accountNumber)
            # Login After Registration
            # auth.login(request, user)
            # messages.success(request, 'You are now logged in')
            # return redirect('index')
                         user.save()
                         messages.success( request, 'You are now registerd and can log in')
                         return redirect('login')

        else:
            messages.error(request, 'Password do not match')
            return redirect('register')
    context = {
        'form': form
    }
    return render(request, 'register/register.html',context)


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Incorrect log in details')
            return redirect('login')

    return render(request, 'register/login.html')

def logout(request):
    if request.method =="POST":
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')