from django import forms

class UserForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=128)
    last_name = forms.CharField(max_length=128)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20)

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)

class ListingForm(forms.Form):
    customer = forms.CharField(max_length=128)
    category = forms.CharField(max_length=128)
    description = forms.CharField()
    cost = forms.CharField()
