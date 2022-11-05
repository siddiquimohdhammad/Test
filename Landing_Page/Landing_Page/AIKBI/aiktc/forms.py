from django import forms
from django.forms import ModelForm
from .models import Form


# Create a registration form
class registrationForm(ModelForm):
    #Define things in the class
    class Meta:
        model = Form
        fields = "__all__"
        