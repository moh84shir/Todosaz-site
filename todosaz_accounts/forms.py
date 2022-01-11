from captcha.widgets import ReCaptchaV2Checkbox
from captcha.fields import ReCaptchaField
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    def login_user(self, request):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        self.add_error("username", "عملیات ورود با شکست مواجه شد")


class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    re_password = forms.CharField(widget=forms.PasswordInput)

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

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
        User.objects.create_user(username=cd["username"], password=cd["password"])
        return redirect("/accounts/login/")


class EditProfileForm(forms.Form):
    first_name = forms.CharField(required=False, label="نام")
    last_name = forms.CharField(required=False, label="نام خانوادگی")
    email = forms.EmailField(required=False, label="ایمیل")

    def edit_profile(self, user):
        cd = self.cleaned_data

        first_name = cd["first_name"] if "first_name" in cd else user.first_name
        last_name = cd["last_name"] if "last_name" in cd else user.last_name
        email = cd["email"] if "email" in cd else user.email
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
