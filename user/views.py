from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse
from App1.models import *
from App1.forms import *
#from datetime import timezone
from django.utils import timezone
from . import views
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.utils.safestring import mark_safe
# Create your views here.
def logi_in(response):    
    first = First()
    last = Last()   
    company =Company()
    email = Email()
    new_password= NewPassword()

    return render(response, 
    'user/register.html',
    {'forming':1,'first': first,'last':last,'company':company,'email':email,'new':new_password})
def home(response):
    if response.method == 'POST':
        first = First(response.POST)
        last = Last(response.POST)   
        company =Company(response.POST)
        email = Email(response.POST)
        new_password= NewPassword(response.POST)
        p = Product.objects.all()
        a=Advertisement.objects.all()
        if response.POST.get('users'):
            kirubel=response.POST.get('users')
            print(kirubel)
            user=User.objects.get(id=int(kirubel))

            return render(response, 'user/home.html',{'user':user,'k':p,'a':a})

        elif (first.is_valid(), last.is_valid(),company.is_valid(), email.is_valid() , new_password.is_valid(),response.POST.get('sign')):

            if response.POST.get('sign'):
                f1 = first.cleaned_data['first_name']
                f2 = last.cleaned_data['last_name']
                f3 = company.cleaned_data['company']
                f4=email.cleaned_data['email']
                f6 = new_password.cleaned_data['new_password']

                try:
                    user=User.objects.get(first_name=f1,last_name=f2,company=f3,email=f4,password=f6)
                    print(str(user))
                    x='success'
                    return render(response, 'user/home.html',{'user':user,'k':p,'a':a})
                except User.DoesNotExist:
                    print('user not found')
                    y='not found'
                    return render(response, 'user/error.html', {'non-user':''})
            

            if response.POST.get('verify'):
                f1 = first.cleaned_data['first_name']
                f2 = last.cleaned_data['last_name']
                f3 = company.cleaned_data['company']
                f4 = email.cleaned_data['email']
                f5 = new_password.cleaned_data['new_password']
                try:
                    user_on=UserOn.objects.get(first_name=f1,last_name=f2,company=f3,email=f4,password=f5)
                    serial=user_on.serial
                    if user_on:

                        user=User(first_name=f1,last_name=f2,company=f3,email=f4,password=f5)
                        user.save()
                        serial.delete()
                        user_on.delete()
                        return render(response, 'user/home.html',{'user':user,'k':p,'a':a})
                    else:
                        return render(response,'user/error.html',{'y':'something went wrong \n it might be incorrect field data,so go back and fill it again'})
                except UserOn.DoesNotExist:
                    print(str(UserOn.DoesNotExist))
                    return render(response,'user/error.html',{'y':'something went wrong'})



        else:
            return render(response, 'user/error.html', {'y':'some thing went wrong'})
        if response.POST.get('comments'):
            u=response.POST.get('comments')
            user=User.objects.get(id=int(u))

            return  render(response, 'user/home.html',{'user':user,'commenter':'l'})
    else:
        return  render(response, 'user/error.html', {'y':'some thing went wrong'})
def order(response):
    p = Product.objects.all()
    a=Advertisement.objects.all()
    if response.method=='POST':
        date=Date(response.POST)
        if response.POST.get('user0'):
            
            kirubel=response.POST.get('user0')
            print(kirubel)
            product=Product.objects.all()
            user=User.objects.get(id=int(kirubel))
            date=Date()
            return render(response,'user/order.html',{'user':user,'date':date,'form':'form','product':product})
        if  date.is_valid() and response.POST.get('use0'):
            kirubel=response.POST.get('use0')
            print(kirubel)
            
            f4 = response.POST.get('product')
            f5 = response.POST.get('amount')
            f6 = response.POST.get('unit')
            f7 = date.cleaned_data['date']
            f8 = response.POST.get('how_many_times')
            try:
                z=Product.objects.get(id=int(f4))
                user=User.objects.get(id=int(kirubel))
                y=Orders(product=z,amount=f5,unit=f6,for_when=f7,how_many_times=f8,) 
                y.user=user
                y.save()
                send_mail(
                        f'new order from {y.user.first_name,y.user.last_name}\n at {timezone.now()}',
                        f'his email is{user.email}\n his orders as follow\n{z.name},{y.amount , y.unit,y.for_when,y.how_many_times}',
                        settings.EMAIL_HOST_USER,
                        [settings.EMAIL_HOST_USER],
                        fail_silently=False,
                    )

                #a=OrderState(order=y,state=False)
                #a.save()
                return render(response,'user/home.html',{'user':user,'k':p,'a':a})
            except( User.DoesNotExist, Product.DoesNotExist):
                print(str(User.DoesNotExist and Product.DoesNotExist))
                return render(response, 'user/error.html', {'y':'some thing went wrong'})
        if response.POST.get('order_home'):
            product_name=response.POST.get('product')
            p=Product.objects.get(id=int(product_name))
            form=OrderingForm()         
            date=Date()
            lit=[]
            lit.append(product_name)
            product=Product.objects.all()
            user=User.objects.get(id=int(response.POST.get('order_home')))
            print(product_name)
            return render(response, 'user/order.html',{'user':user,'form':form,'date':date,'li':lit,'product':product,'productc':p})


    else:
        return render(response,'user/error.html',{'y','some thing went wrong'})
def about(response):
    if response.method=='POST':
        if response.POST.get('user1'):
            l=[]
            k={i.name:k.url for i in link.objects.all() for k in link.objects.all()}
            posts={i.index:k for i in PostLink.objects.all()}
            info=FromComp.objects.all()
            for i in info:
                k=i.post
                l.append(k)
            kirubel=response.POST.get('user1')
            print(kirubel)
            user=User.objects.get(id=int(kirubel))
            return render(response,'user/about.html',{'user':user,'k':l})
    else:
        return render(response,'user/error.html',{'y','some thing went wrong'})
def community(response):
    if response.method=='POST':
        if response.POST.get('usersh'):
            k = CommentsB.objects.all()
            kirubel=response.POST.get('usersh')
            print(kirubel)
            user=User.objects.get(id=int(kirubel))
            return render(response,'user/community.html',{'user':user,'k':k})
    else:
        return render(response,'user/error.html',{'y','some thing went wrong'})
def setting(response):
    if response.method=='POST':
        if response.POST.get('user2'):
            kirubel=response.POST.get('user2')
            print(kirubel)
            user=User.objects.get(id=int(kirubel))
            orders=[]
            for i in user.orders_set.all():
                orders.append(i)
            return render(response,'user/setting.html',{'user':user,'order':orders})
        else:
            kirubel=response.POST.get('user2')
            print(kirubel)
            return render(response,'user/error.html',{'y':'some thing went wrong'})
    else:
        return render(response,'user/error.html',{'y':'some thing went wrong'})

    