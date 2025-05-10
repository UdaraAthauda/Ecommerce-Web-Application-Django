from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, SetPasswordForm
from django.forms.widgets import TextInput, PasswordInput
from .models import *

# user login form
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput)
    password = forms.CharField(widget=PasswordInput)

# user signup form
class SignUpForm(UserCreationForm):
    phone = forms.CharField(max_length=15, required=True)
    address = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'address', 'password1', 'password2',)

# user detail update form
class UserUpdateForm(UserChangeForm):
    phone = forms.CharField(max_length=15, required=True)
    address = forms.CharField(widget=forms.Textarea, required=True)
    password = None

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'address',)

# user password change form
class PasswordChangeForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ('new_password1', 'new_password2',)