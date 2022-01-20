from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render

from .forms import ChangeSettingsFrom
from .models import Setting


def change_settings(request):
    if request.user.is_superuser:
        settings = Setting.objects.last()

        if settings is None:
            Setting.objects.create(
                title="", short_desc="", about="", email="", phone="")

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
