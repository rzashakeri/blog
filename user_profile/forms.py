from django import forms
from django.core import validators


class EditProfileForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'user-profile__item-input'
    }),
        required=True,
        error_messages={
            'required': 'first_name is required'
        },
        validators=[
            validators.MinLengthValidator(3)
        ])

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'user-profile__item-input'
    }),
        required=True,
        error_messages={
            'required': 'last name is required'
        },
        validators=[
            validators.MinLengthValidator(3)
        ])

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'user-profile__item-input'
    }),
        required=True,
        error_messages={
            'required': 'email is required'
        },
        validators=[
            validators.EmailValidator
        ])

    about_us = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'user-profile__item-input user-profile__textarea'
    }),
        validators=[
            validators.MaxLengthValidator(150)
        ])
