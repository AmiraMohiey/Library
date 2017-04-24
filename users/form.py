from django.contrib.auth.models import User
from django import  forms


class RegisterationForm(forms.ModelForm):
    class Meta:
        password = forms.CharField(widget=forms.PasswordInput)
        model=User
        fields=['first_name','email','username','password']


class LoginForm(forms.ModelForm):
    class Meta:
        password = forms.CharField(widget=forms.PasswordInput)
        model = User
        fields = ['username','password']

