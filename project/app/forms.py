from django import forms
from .models import caravailability
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class carquery(forms.ModelForm):
    class Meta:
        model = caravailability
        fields = "__all__"
        labels ={
            "email": "Your Email",
            "first_name": "Your first name",
            "last_name": "Your last name",
            "description": "Send some text about your order",
            "car_select": "Choose the Car"
            

        }

        error_messages = {
            "email" :{
                "required": "Your email must not be empty",
                "max_lenght": "Please enter a shorter email!",
            },
            "first_name" :{
                "required": "Your name must not be empty",
                "max_lenght": "Please enter a shorter name!",
            },
            "last_name": {
                "required": "Your name must not be empty",
                "max_lenght": "Please enter a shorter name!",
            },
            "description" :{
                "max_lenght": "Please enter a shorter text!",
            }
        }



class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
   remember_me = forms.BooleanField(
       required=False,
       initial=True,
       widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
   )