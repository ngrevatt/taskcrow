from django import forms
from django.forms.extras.widgets import SelectDateWidget
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class UserForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=128)
    last_name = forms.CharField(max_length=128)
    email = forms.EmailField()
    phone_number = PhoneNumberField(required=False, widget=PhoneNumberPrefixWidget)


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)


class ListingForm(forms.Form):
    description = forms.CharField()
    category = forms.IntegerField()
    cost = forms.IntegerField()
    due_date = forms.DateTimeField(widget=SelectDateWidget)
