from django.views.generic.edit import FormView, UpdateView
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, EditProfileForm
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


@login_required
def user_profile(request):
    user = request.user
    username = user.username
    first_name = user.first_name
    last_name = user.last_name
    email = user.email

    context = {
        "user":user,
        "username": username,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
    }
    return render(request, 'accounts/profile.html', context)

# class EditProfile(FormView):
#     form_class = EditProfileForm
#     success_url = "/accounts/profile/"
#     template_name = "accounts/edit_profile.html"

#     def form_valid(self, form):
#         form.edit_profile(self.request.user)
#         return super().form_valid(form)


class EditProfile(UpdateView):
    fields = ['first_name', 'last_name', 'email']
    success_url = "/accounts/profile/"
    template_name = "accounts/edit_profile.html"

    def get_queryset(self):
        username = self.request.user.username
        return User.objects.filter(username=username)