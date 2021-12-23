from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied

from todosaz_settings.models import Setting
from .forms import ChangeSettingsFrom
from django.views.generic.base import View
from django.views.generic.edit import UpdateView


def change_settings(request):
    if request.user.is_superuser:
        form = ChangeSettingsFrom(request.POST or None)
        if form.is_valid():
            form.change_settings()
            return redirect("/")
        return render(request, "settings/change.html", {"form": form})
    raise PermissionDenied
