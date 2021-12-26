from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render

from todosaz_settings.models import Setting

from .forms import ChangeSettingsFrom


def change_settings(request):
    if request.user.is_superuser:
        settings = Setting.objects.last()
        form = ChangeSettingsFrom(
            request.POST or None,
            initial={
                "title": settings.title,
                "short_desc": settings.short_desc,
                "about": settings.about,
                "email": settings.email,
                "phone": settings.phone,
            },
        )
        if form.is_valid():
            form.change_settings()
            return redirect("/")
        return render(request, "settings/change.html", {"form": form})
    raise PermissionDenied


def rest_settings(request):
    if request.user.is_superuser:
        settings = Setting.objects.all()
        if settings is not None:
            settings.delete()
            Setting.objects.create()
        return redirect('/settings/change/')
    raise PermissionDenied
