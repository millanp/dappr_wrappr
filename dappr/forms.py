from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from django.contrib.auth.models import User
from django import forms
class RegistrationForm(UserCreationForm):
    email = fields.EmailField(required=True)
    email1 = fields.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ("username", "email")
    
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        email = cleaned_data.get("email")
        email1 = cleaned_data.get("email1")
        if email and email1 and email != email1:
            raise forms.ValidationError("Email addresses do not match")