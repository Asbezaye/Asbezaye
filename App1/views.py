from django.urls import get_script_prefix, reverse
from . import views
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.utils.safestring import mark_safe
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from django.contrib.sites.shortcuts import get_current_site

k = list()
s = Serial.objects.all()
for i in s:
    k.append(i.code)


# Create your views here.
def home(response):
    p = Product.objects.all()
    a=Advertisement.objects.all()
    return render(response, 'App1/home.html', {'k': p,'a':a})


def order(response):
    if response.method == 'POST':
        date=Date(response.POST)
        form = OrderingForm(response.POST)
        if form.is_valid() and date.is_valid():
            f1 = form.cleaned_data['first_name']
            f2 = response.POST.get('email')
            f3 = response.POST.get('password')
            f4 = response.POST.get('product')
            f5 = response.POST.get('amount')
            f6 = response.POST.get('unit')
            f7 = date.cleaned_data['date']
            f8 = response.POST.get('how_many_times')
            try:
                k=User.objects.get(first_name=f1,email=f2,password=f3)
                z=Product.objects.get(id=int(f4))
                y=Orders(product=z,amount=f5,unit=f6,for_when=f7,how_many_times=f8) 
                y.user=k
                y.save()
                send_mail(
                    f'new order from {y.user.first_name,y.user.last_name}\n at {timezone.now()}',
                    f'his email is{y.user.email}\n his orders as follow\n{z.name},{y.amount , y.unit,y.for_when,y.how_many_times}',
                    settings.EMAIL_HOST_USER,
                    [settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
                
                return redirect(views.home)
            except( User.DoesNotExist, Product.DoesNotExist):
                print(str(User.DoesNotExist or Product.DoesNotExist))
                return render(response, 'user/error.html', {'y':'some thing went wrong'})


        if response.POST.get('order_home'):
            product_name=response.POST.get('order_home')
            p=Product.objects.get(name=product_name)
            form=OrderingForm()         
            date=Date()
            lit=[]
            lit.append(product_name)
            product=Product.objects.all()
            return render(response, 'App1/order.html', {'form':form,'date':date,'li':lit,'product':product,'productc':p})
            
    else:  
        form=OrderingForm()         
        y=0
        date=Date()
        product=Product.objects.all()
        return render(response, 'App1/order.html', {'form':form,'date':date,'product':product,'k':y})


def sign_in(response):
    if response.method == 'POST':
        first = First(response.POST)
        last = Last(response.POST)   
        company =Company(response.POST)
        email = Email(response.POST)
        new_password= NewPassword(response.POST)
        confirm=Confirm(response.POST)
        serial= Serials(response.POST)
        if (first.is_valid(), last.is_valid(),company.is_valid(), email.is_valid() , new_password.is_valid() , confirm.is_valid(), serial.is_valid() ):
            f1 = first.cleaned_data['first_name']
            f2 = last.cleaned_data['last_name']
            f3 = company.cleaned_data['company']
            f4=email.cleaned_data['email']
            f5 = serial.cleaned_data['serial']
            f6 = new_password.cleaned_data['new_password']
            f7= confirm.cleaned_data['confirm_password']
            if int(f5) in k and f6==f7:

                user = UserOn(first_name=f1,
                              last_name=f2,
                              company=f3,
                              email=f4,
                              )
                seral=Serial.objects.get(code=f5)
                user.serial=seral
                user.password = f6
                user.save()

                # I need to add emailing functionality
                if user.save():

                    send_mail(
                        'verify your email',
                        'click this link to fully register\n'+mark_safe('<button type="link" href='+str(get_current_site(response).domain+reverse('verify',args=[user.serial.code]))+'> verify<button>'),
                        settings.EMAIL_HOST_USER,
                        [f4],
                        fail_silently=False,
                    )
                return render(response, 'App1/sign_in.html', {'sent': user})

            elif f5 not in k:
                first = First()
                last = Last()   
                company =Company()
                email = Email()
                new_password= NewPassword()
                confirm=Confirm()
                serial= Serials()
                return render(response, 'App1/sign_in.html', {'forming':'1','ac_code': 'l','first': first,'last':last,'company':company,'email':email,'new':new_password,'confirm':confirm,'serial':serial})
            elif f6 !=f7:
                return render(response, 'App1/sign_in.html', {'forming':1,'password_not': '1'})
            else:
                return render(response, 'user/error.html', {'y': 'some thing went wrong'})
    first = First()
    last = Last()   
    company =Company()
    email = Email()
    new_password= NewPassword()
    confirm=Confirm()
    serial= Serials()
    return render(response, 
    'App1/sign_in.html',{'forming':1,'first': first,'last':last,'company':company,'email':email,'new':new_password,'confirm':confirm,'serial':serial})


def search(response, page=int):
    return render(response, 'App1/results.html', {})


def new_code(response):
    return render(response, 'App1/new_code.html', {})


def verify(response,ss=int):
    if response.method=='POST':

        return render(response,'user/error.html',{'y':'something went wrong'})

    else:
        try:
            use=Serial.objects.get(code=ss)
            useron=UserOn.objects.get(serial=use)
            first = First()
            last = Last()   
            company =Company()
            email = Email()
            new_password= NewPassword()
            return render(response, 'App1/validate.html', {'user':useron,'first': first,'last':last,'company':company,'email':email,'new':new_password,})
        except UserOn.DoesNotExist:
            print('user not found')
            return render(response,'user/error.html',{'y':'something went wrong'})



def about(response):
    l=[]
    info=FromComp.objects.all()
    for i in info:
        k=i.post
        l.append(k)

    return render(response, 'App1/about.html', {'k':l})


def community(response):
    k = CommentsB.objects.all()
    return render(response, 'App1/community.html', {'k': k})



