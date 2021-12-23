from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.list import ListView
from django.views.generic.base import View
from .models import New
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .forms import CreateNewForm


class SuperUserRequired(View):
    """
    parend class for check is superuser
    (in class base views!!!)
    """

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


# Create Read Delete Update

# Read => list view, detail view

# List View
class NewsList(ListView):
    """show the active news list"""

    queryset = New.objects.filter(is_active=True)
    template_name = "news/news_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # send "is_superuser" to template
        context["is_superuser"] = self.request.user.is_superuser
        return context


# Detail View
def new_detail(request, pk):
    """show the active new"""
    new = get_object_or_404(New, pk=pk, is_active=True)
    return render(request, "news/new_detail.html", {"new": new, "user": request.user})


# Create new
@login_required
def create_new(request):
    """submit an news"""
    if request.user.is_superuser:  # check user permission
        form = CreateNewForm(request.POST or None)
        if form.is_valid():
            form.create_new()
            return redirect("/news/")
        return render(request, "news/create_new.html", {"form": form})
    raise PermissionDenied  # 403 (forbidden)


# Delete new
@login_required
def delete_new(request, pk):
    """delete an news"""
    if request.user.is_superuser:  # check user permission
        new = get_object_or_404(New, pk=pk)
        new.delete()
        return redirect("/news/")
    raise PermissionDenied  # 403 (forbidden)


# Update new
class UpdateNew(SuperUserRequired, UpdateView):
    """edit an news (inheritance from 'CheckSuperUser' for check permission)"""

    model = New
    fields = ["title", "short_desc", "text", "is_active"]
    template_name = "news/update_new.html"
    success_url = "/news/"
