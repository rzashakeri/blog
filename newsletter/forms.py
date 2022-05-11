from django import forms
from django.core import validators


class NewsletterForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'newsletter__input',
        'placeholder': 'email'
    }),
        required=True,
        error_messages={
            'required': 'email is required'
        },
        validators=[
            validators.EmailValidator
        ])
