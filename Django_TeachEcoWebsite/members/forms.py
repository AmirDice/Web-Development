from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms

from personal.models import Comment


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_superuser = forms.CharField(
        max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_staff = forms.CharField(
        max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_active = forms.CharField(
        max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'is_superuser', 'is_staff', 'is_active']


class CommentForm(forms.ModelForm):
    # first_name = forms.CharField(
    #     max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # last_name = forms.CharField(
    #     max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # body = forms.CharField(
    #     max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
