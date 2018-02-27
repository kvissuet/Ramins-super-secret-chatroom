from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  
from .models import Profile
from django.db.models import F

class SignUpForm(UserCreationForm):
    shift=forms.CharField(max_length=2,help_text='Number between 1 and 25')
    class Meta:
        model = User
        fields = ('username',  'password1', 'password2', 'shift')
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('shift', 'prime_1', 'prime_2')

        