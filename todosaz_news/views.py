from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.base import View
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import CreateNewForm
from .models import New


class SuperUserRequired(View):
    """
    parend class for check is superuser
    (only in class base views!!!)
    """

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class NewsList(ListView):
    """ show the active news list """
    model = New
    template_name = "news/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_superuser"] = self.request.user.is_superuser
        return context


def new_detail(request, pk):
    """show the active new"""
    new = get_object_or_404(New, pk=pk)
    return render(request, "news/detail.html", {"new": new, "user": request.user})


@login_required
def create_new(request):
    """submit an news"""
    if request.user.is_superuser:
        form = CreateNewForm(request.POST or None)
        if form.is_valid():
            form.create_new()
            return redirect("/news/")
        return render(request, "news/create.html", {"form": form})
    raise PermissionDenied


@login_required
def delete_new(request, pk):
    """delete an news"""
    if request.user.is_superuser:
        new = get_object_or_404(New, pk=pk)
        new.delete()
        return redirect("/news/")
    raise PermissionDenied


class DeleteNew(DeleteView, SuperUserRequired):
    model = New
    template_name = 'news/delete.html'
    success_url = '/news/'


class UpdateNew(SuperUserRequired, UpdateView):
    """edit an news """

    model = New
    fields = ["title", "short_desc", "text", "is_active"]
    template_name = "news/update.html"
    success_url = "/news/"
