from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]
        # exclude = ['fist_name']
        labels = {
            'username': 'Username',
            'first_name': 'Fist name',
            'last_name': 'Last name',
            'email': 'E-mail',
            'password': 'Password',
        }
        help_texts = {
            'email': 'The email must be valid'
        }
        error_messages = {
            'username': {
                'required': 'This field must not be empty'
            }
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Type your user'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Type your password here'
            })
        }
