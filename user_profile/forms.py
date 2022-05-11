from django import forms
from django.core import validators
from user_management.models import User


class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'about_us']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'user-profile__item-input'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'user-profile__item-input'
            }),
            'email': forms.TextInput(attrs={
                'class': 'user-profile__item-input'
            }),
            'about_us': forms.Textarea(attrs={
                'class': 'user-profile__item-input user-profile__textarea'
            })
        }
        error_messages = {
            'first_name': {
                'required': 'first_name is required'
            },
            'last_name': {
                'required': 'last name is required'
            },
            'email': {
                'required': 'email is required'
            }
        }
        labels = {
            'first_name': 'Name',
            'last_name': 'Family',
            'email': 'Email',
            'about_us': 'About'
        }