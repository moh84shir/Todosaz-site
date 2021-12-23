from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login(request):
    if not request.user.is_authenticated:
        form = LoginForm(request.POST or None)
        if form.is_valid():
            form.login_user(request)
        return render(request, "accounts/login.html", {"form": form})
    return redirect("/")


def register(request):
    if not request.user.is_authenticated:
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            form.register_user()
        return render(request, "accounts/register.html", {"form": form})
    return redirect("/")


@login_required
def del_account(request):
    loggedin_user = request.user
    if not loggedin_user.is_authenticated:
        return redirect("/accounts/login/")
    User.objects.delete(loggedin_user)
    return redirect("/accounts/register/")
