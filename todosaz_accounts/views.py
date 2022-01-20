from .models import AboutUser
from django.urls import reverse
from django.views.generic.edit import UpdateView
from django.shortcuts import render, redirect
from .models import ProfileImage
from todosaz_todoes.models import Todo
from .forms import LoginForm, RegisterForm, AddOrChangeProfileImageForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def login(request):
    next_url = request.GET['next'] if 'next' in request.GET else '/'
    if not request.user.is_authenticated:
        form = LoginForm(request.POST or None)
        if form.is_valid():
            form.login_user(request)
            return redirect(next_url)
        return render(request, 'accounts/login.html', {'form': form})
    return redirect(next_url)


def register(request):
    next_url = request.GET['next'] if 'next' in request.GET else '/'
    if not request.user.is_authenticated:
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            form.register_user()
        return render(request, 'accounts/register.html', {'form': form})
    return redirect(next_url)


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
        about = AboutUser.objects.get(user=user).about
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
        'about':about,
    }
    return render(request, 'accounts/profile.html', context)


class EditProfile(UpdateView):
    fields = ['first_name', 'last_name', 'email']
    success_url = '/accounts/profile/'
    template_name = 'accounts/edit_profile.html'

    def get_queryset(self):
        username = self.request.user.username
        return User.objects.filter(username=username)


@login_required
def logout_user(request):
    logout(request)
    return redirect('/accounts/login/')


@login_required(login_url='/accounts/login/')
def change_profile_image(request):
    '''
        create user profile if not exists 
        and change user profile if exists
    '''
    if request.method == 'POST':
        form = AddOrChangeProfileImageForm(request.POST, request.FILES)
        if form.is_valid():
            ProfileImage.objects.create(
                image=request.FILES['image'], user=request.user)

            # Redirect to the document list after POST
            return redirect(reverse('accounts:profile'))
    else:
        form = AddOrChangeProfileImageForm(
            request.POST, request.FILES)  # An empty, unbound form

    context = {'form': form}  # send form if get method of request
    return render(request, 'accounts/change_profile.html', context)
