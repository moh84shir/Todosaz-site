from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django.urls import reverse


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


class RegisterForm(forms.Form):
    username = forms.CharField(label="نام کاربری")
    password = forms.CharField(widget=forms.PasswordInput, label="رمز عبور")
    re_password = forms.CharField(
        widget=forms.PasswordInput, label="تایید رمز عبور")
    captcha = ReCaptchaField(
        widget=ReCaptchaV2Checkbox, label="تایید گوگل کپچا")

    def clean_re_password(self):
        cd = self.cleaned_data
        if cd["password"] != cd["re_password"]:
            raise forms.ValidationError("رمز های عبور مطابقت ندارند")
        return cd["password"]

    def clean_username(self):
        username = self.cleaned_data.get("username")
        is_username_exists = User.objects.filter(username=username).exists()

        if is_username_exists:
            raise forms.ValidationError("نام کاربری تکراریست")

        return username

    def register_user(self):
        cd = self.cleaned_data
        User.objects.create_user(
            username=cd["username"], password=cd["password"])
        return redirect(reverse('accounts:login'))


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
