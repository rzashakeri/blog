from django import forms


class RegisterForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'register__form-item register__first-name',
        'placeholder': 'name'
    }),
        required=True,
        error_messages={
            'required': 'email field required'
        },
    )

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'register__form-item register__last-name',
        'placeholder': 'family'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'register__form-item register__email',
        'placeholder': 'email'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'register__form-item register__password',
        'placeholder': 'password'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'register__form-item register__confirm-password',
        'placeholder': 'confirm password'
    }))
