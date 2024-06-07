from django import forms
from authApp.models import User

class RegisterForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=255)


class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email']


