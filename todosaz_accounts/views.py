from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import UpdateView
from todosaz_todoes.models import Todo

from .forms import (AddOrChangeProfileImageForm, ChangeAboutForm, LoginForm,
                    RegisterForm,)
from .models import AboutUser, ProfileImage
from django.views.generic.edit import FormView
from django.contrib.auth.views import PasswordChangeView, LoginView


class Login(LoginView):
    template_name = 'accounts/login.html'


# def login(request):
#     next_url = request.GET['next'] if 'next' in request.GET else reverse(
#         'accounts:profile')
#     if not request.user.is_authenticated:
#         form = LoginForm(request.POST or None)
#         if form.is_valid():
#             form.login_user(request)
#             return redirect(next_url)
#         return render(request, 'accounts/login.html', {'form': form})
#     return redirect(next_url)

from django.views.generic.edit import CreateView

class Register(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/register.html'


@login_required
def del_account(request):
    loggedin_user = request.user.username
    User.objects.get(username=loggedin_user).delete()
    return redirect('/accounts/register/')


@login_required
def user_profile(request):
    user = request.user
    username = user.username
    first_name = user.first_name
    last_name = user.last_name
    email = user.email
    profile_image = ProfileImage.objects.filter(user=user).last()
    todo_count = Todo.objects.filter(user=user).count()
    try:
        about = AboutUser.objects.filter(user=user).last().about
    except:
        about = None

    context = {
        'user': user,
        'username': username,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'todo_count': todo_count,
        'profile_image': profile_image,
        'about': about,
    }
    return render(request, 'accounts/profile.html', context)


class EditProfile(UpdateView):
    fields = ['first_name', 'last_name', 'email']
    success_url = '/accounts/profile/'
    template_name = 'accounts/edit_profile.html'

    def get_queryset(self):
        username = self.request.user.username
        return User.objects.filter(username=username)


class SetPassword(PasswordChangeView):
    template_name = 'accounts/change_password.html'
    success_url = '/accounts/profile/'


@login_required
def logout_user(request):
    logout(request)
    return redirect('/accounts/login/')


@login_required(login_url='/accounts/login/')
def change_profile_image(request):
    if request.method == 'POST':
        form = AddOrChangeProfileImageForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            ProfileImage.objects.filter(user=user).delete()

            ProfileImage.objects.create(
                image=request.FILES['image'], user=request.user)

            # Redirect to the document list after POST
            return redirect(reverse('accounts:profile'))
    else:
        form = AddOrChangeProfileImageForm(
            request.POST, request.FILES)  # An empty, unbound form

    context = {'form': form}  # send form if get method of request
    return render(request, 'accounts/change_profile.html', context)


@login_required
def edit_about(request):
    user = request.user
    about_object = AboutUser.objects.filter(user=user).last()
    form = ChangeAboutForm(request.POST or None, initial={
                           'about': about_object.about})
    if form.is_valid():
        cd = form.cleaned_data

        about_object.about = cd['about']
        about_object.save()
        return redirect(reverse('accounts:profile'))

    return render(request, 'accounts/edit_about.html', {'form': form})
