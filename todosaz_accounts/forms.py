from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def login_user(self, request):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/todoes/")
        self.add_error("username", "عملیات ورود با شکست مواجه شد")


class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    re_password = forms.CharField(widget=forms.PasswordInput)

    def clean_re_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['re_password']:
            raise forms.ValidationError("رمز های عبور مطابقت ندارند")
        return cd['password']

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
