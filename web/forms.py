# --------------------------------------------------------------------------- #
# Django exceptions
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
# --------------------------------------------------------------------------- #
# Models
from .models import UserModel, VideosModel, Commentsmodel
# --------------------------------------------------------------------------- #
# Translation
from django.utils.translation import gettext_lazy as _

# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
# User Model Form
class AccountForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'email', 'user_image']


class VideosForm(forms.ModelForm):
    class Meta:
        model = VideosModel
        exclude = ('created_at', 'updated_at', 'user')
        
class CommentsForm(forms.ModelForm):
    class Meta:
        model = Commentsmodel
        fields = ['text']

# --------------------------------------------------------------------------- #
# Login
class LoginForm(forms.Form):
    username = forms.CharField(max_length=16, widget=forms.TextInput(attrs={
        'placeholder': _('Enter your username')
    }))

    password = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={
        'placeholder': _('Enter you password')
    }))

    class Meta:
        model = UserModel
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


# --------------------------------------------------------------------------- #
# Registration
class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean_confirm_password(self):
        if self.cleaned_data['confirm_password'] != self.cleaned_data['password']:
            raise ValidationError('Passwords do not same')
        return self.cleaned_data['confirm_password']

    def clean_username(self):
        try:
            user = UserModel.objects.get(username=self.cleaned_data['username'])
            if user:
                raise ValidationError('This username is already in use')
        except:
            return self.cleaned_data['username']


# --------------------------------------------------------------------------- #