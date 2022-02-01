from .models import AboutUser
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(label="نام کاربری")
    password = forms.CharField(widget=forms.PasswordInput, label="رمز عبور")
    captcha = ReCaptchaField(
        widget=ReCaptchaV2Checkbox, label="تایید گوگل کپچا")

    def login_user(self, request):
        cd = self.cleaned_data
        user = authenticate(username=cd["username"], password=cd["password"])
        if user is not None:
            login(request, user)
        self.add_error("username", "عملیات ورود با شکست مواجه شد")


class RegisterForm(UserCreationForm):
    pass


class EditProfileForm(forms.Form):
    first_name = forms.CharField(required=False, label="نام")
    last_name = forms.CharField(required=False, label="نام خانوادگی")
    email = forms.EmailField(required=False, label="ایمیل")

    def edit_profile(self, user):
        cd = self.cleaned_data

        user.first_name = cd['first_name']
        user.last_name = cd['last_name']
        user.email = cd['email']
        user.save()


class AddOrChangeProfileImageForm(forms.Form):
    image = forms.ImageField(
        label="لطفا پروفایل جدید خودتان را انتخاب کنید",
    )


class ChangeAboutForm(forms.Form):
    about = forms.CharField(
        label="درباره ی شما"
    )
