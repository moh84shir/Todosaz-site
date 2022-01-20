from django.shortcuts import render


def home(request):
    user = request.user

    context = {
        'is_authenticated': user.is_authenticated
    }
    return render(request, 'index.html', context)