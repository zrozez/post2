from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from django.forms.widgets import TextInput
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.TextInput())

class CreateLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.TextInput())
