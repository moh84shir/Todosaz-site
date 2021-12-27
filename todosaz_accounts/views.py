from django.views.generic.edit import UpdateView
from django.shortcuts import render, redirect

from todosaz_todoes.models import Todo
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def login(request):
    if not request.user.is_authenticated:
        form = LoginForm(request.POST or None)
        if form.is_valid():
            form.login_user(request)
            return redirect('/')
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


@login_required
def user_profile(request):
    user = request.user
    username = user.username
    first_name = user.first_name
    last_name = user.last_name
    email = user.email
    todo_count = Todo.objects.filter(user=user).count()

    context = {
        "user": user,
        "username": username,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "todo_count": todo_count,
    }
    return render(request, "accounts/profile.html", context)


class EditProfile(UpdateView):
    fields = ["first_name", "last_name", "email"]
    success_url = "/accounts/profile/"
    template_name = "accounts/edit_profile.html"

    def get_queryset(self):
        username = self.request.user.username
        return User.objects.filter(username=username)


@login_required
def logout_user(request):
    logout(request)
    return redirect("/accounts/login/")
