from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import Orders, Product



class First(forms.Form):
    first_name = forms.CharField( min_length=3, label=False,max_length=100,widget=forms.TextInput(attrs={
        'class':'form-control  bg-dark',
        'aria-describedby':"basic-addon2",
        'placeholder':"Your first name",
        'style':'color:green;',
    }))


class Last(forms.Form):
    last_name = forms.CharField(min_length=3, label=False,max_length=60,widget=forms.TextInput(attrs={
    'class':'form-control bg-dark',
    'aria-describedby':"basic-addon2",
    'placeholder':"Your last name",
    'style':'color:green;',
}))


class Company(forms.Form):
    company = forms.CharField(max_length=80,label=False, required=False,widget=forms.TextInput(attrs={
    'class':'form-control bg-dark',
    'aria-describedby':"basic-addon2",
    'placeholder':"Your company's name",
    'style':'color:green;',
}))


class Email(forms.Form):
    email = forms.EmailField(max_length=60,label=False,widget=forms.TextInput(attrs={
    'class':'form-control bg-dark',
    'type':'email',
    'aria-describedby':"basic-addon2",
    'placeholder':"Your email address",
    'style':'color:green;',
}))


class NewPassword(forms.Form):

    new_password =forms.CharField( min_length=5,label=False, max_length=100,widget=forms.TextInput(attrs={
    'class':'form-control bg-dark',
    'type':'password',
    'aria-describedby':"basic-addon2",
    'placeholder':"Create strong password",
    'style':'color:green;',
}))


class Confirm(forms.Form):
    confirm_password =forms.CharField( min_length=5,label=False, max_length=100,widget=forms.TextInput(attrs={
    'class':'form-control bg-dark',
    'type':'password',
    'aria-describedby':"basic-addon2",
    'placeholder':"It must identical",
    'style':'color:green;',
}))


class Serials(forms.Form):
    serial = forms.CharField(max_length=10,required=True,label=False, widget=forms.TextInput(attrs={
    'class':'form-control bg-dark',
    'type':'int',
    'aria-describedby':"basic-addon2",
    'placeholder':"The activation code",
    'style':'color:green;',
}))


class Register(forms.Form):
    first_name = forms.CharField(label='Your first name:', min_length=3, max_length=100)
    last_name = forms.CharField(min_length=3, max_length=60, label='your last name:')
    company = forms.CharField(max_length=80, required=False,help_text='optional')
    email = forms.EmailField(max_length=60, label=' your Email')
    password =forms.CharField(label='password', min_length=5, max_length=100)


class OrderingForm(forms.Form):
    first_name=forms.CharField(label=False,widget=forms.TextInput(attrs={
        'class':'form-control bg-dark',
        'aria-describedby':"basic-addon2",
        'placeholder':"Your first name",
        'style':'color:green;',
    }), min_length=3, max_length=100,required=True)


class Date(forms.Form):
    date=forms.DateField(widget=forms.DateInput(attrs={'type':'date','format':'%Y-%m-%d',
            'class':'form-control bg-dark',
            
            'aria-label':"Password",
        'aria-describedby':"basic-addon2",
        'style':'color:green;',
        
    }),label=False)