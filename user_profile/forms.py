from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core import validators
from django.core.exceptions import ValidationError

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


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'user-profile__item-input'
    }),
        required=True,
        error_messages={
            'required': 'old password is required'
        },
        label='old password',
        validators=[
            validate_password
        ])

    new_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'user-profile__item-input'
    }),
        required=True,
        error_messages={
            'required': 'new password is required'
        },
        label='new password',
        validators=[
            validate_password
        ])

    confirm_new_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'user-profile__item-input'
    }),
        required=True,
        error_messages={
            'required': 'confirm password is required'
        },
        label='confirm password',
        validators=[
            validate_password
        ])

    def clean_confirm_new_password(self):
        new_password = self.cleaned_data.get('new_password')
        confirm_new_password = self.cleaned_data.get('confirm_new_password')
        if new_password == confirm_new_password:
            return confirm_new_password
        raise ValidationError('password and confirm password Do not match')

