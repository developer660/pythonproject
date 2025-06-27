from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import personaldetail

# # Create your views here.
def loggin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('details:form')
        else:
            messages.info(request,"invalid user")
            return redirect('details:loggin')
    return render(request,'login.html')

def registration(request):
    if request.method == 'POST':
        username=request.POST['username']
        firstname = request.POST['First name']
        lastname = request.POST['Last name']
        email= request.POST['Email']
        password = request.POST['password']
        cnfrmpasswrd = request.POST['password1']
        if password==cnfrmpasswrd:
            if User.objects.filter(username=username).exists():
                messages.info(request,"The username already exits")
                return redirect('details:registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "The Email ID already exits")
                return redirect('details:registration')
            else:
                user=User.objects.create_user(username=username,password=password,first_name= firstname,last_name= lastname,email=email)

                user.save();
                return redirect('details:loggin')

        else:
            messages.info(request, "The password is incorrect")
            return redirect('details:registration')
        return redirect('/')
    return render(request,"add.html")

def form(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        billingaddress= request.POST['billingaddress']
        youraddress= request.POST['youraddress']
        state = request.POST['state']
        district = request.POST['topic']
        subdistrict= request.POST['chapter']
        reg= personaldetail.objects.create(firstname=firstname,lastname=lastname,email=email,billingaddress=billingaddress,phonenumber=phonenumber,youraddress=youraddress,state=state,district=district,subdistrict=subdistrict)
        reg.save();

        if reg is not None:
            return redirect('details:payment')
        else:
            messages.info(request, "invalid user")
            return redirect('details:form')
    return render(request, 'form.html')

def payment(request):
    return render(request,'payment.html')

def cnfrm(request):
    return render(request,'cnfrm.html')