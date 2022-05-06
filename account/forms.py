from django import forms
from django.core import validators
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'register__form-item register__first-name',
        'placeholder': 'name'
    }),
        required=True,
        error_messages={
            'required': 'first name field required'
        },
        validators=[
            validators.MinLengthValidator(3),
            validators.MaxLengthValidator(10)
        ]
    )

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'register__form-item register__last-name',
        'placeholder': 'family'
    }),
        required=True,
        error_messages={
            'required': 'last name is required'
        },
        validators=[
            validators.MinLengthValidator(3),
            validators.MaxLengthValidator(10)
        ]
    )

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'register__form-item register__email',
        'placeholder': 'email'
    }),
        required=True,
        error_messages={
            'required': 'email field is required'
        },
        validators=[
            validators.EmailValidator('please enter valid email'),
            validators.MinLengthValidator(4)
        ]
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'register__form-item register__password',
        'placeholder': 'password'
    }),
        required=True,
        error_messages={
            'required': 'password field is required'
        },
        validators=[
            validate_password,
            validators.MinLengthValidator(8, 'password must be 8 characters')
        ])

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'register__form-item register__confirm-password',
        'placeholder': 'confirm password'
    }),
        required=True,
        error_messages={
            'required': 'confirm password is required'
        },
        validators=[
            validate_password,
            validators.MinLengthValidator(8, 'confirm password must be 8 characters')
        ])

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if confirm_password == password:
            return confirm_password
        raise ValidationError('password and confirm password Do not match ')


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'register__form-item register__email',
        'placeholder': 'email'
    }),
        required=True,
        error_messages={
            'required': 'email field is required'
        },
        validators=[
            validators.EmailValidator
        ])

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'register__form-item register__password',
        'placeholder': 'password'
    }),
        required=True,
        error_messages={
            'required': 'password is required'
        },
        validators=[
            validate_password,
            validators.MinLengthValidator(8, 'password must be 8 characters')
        ])
