from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, FormView
from .models import Todo
from .forms import CreateTodoForm


class TodoList(ListView):
    template_name = "todoes/list.html"

    def get_queryset(self):
        usr = self.request.user
        return Todo.objects.filter(user=usr).order_by("-pk")


class TodoDetail(DetailView):
    model = Todo
    template_name = "todoes/detail.html"

    def get_queryset(self):
        usr = self.request.user
        return Todo.objects.filter(user=usr)


class CreateTodo(FormView):
    form_class = CreateTodoForm
    success_url = "/todoes/"
    template_name = "todoes/create.html"

    def form_valid(self, form):
        form.create_todo(user=self.request.user)
        return super().form_valid(form)


class UpdateTodo(UpdateView):
    fields = ["title", "simple_desc", "text"]
    template_name = "todoes/update.html"
    success_url = "/todoes/"

    def get_queryset(self):
        usr = self.request.user
        return Todo.objects.filter(user=usr)


class DeleteTodo(DeleteView):
    model = Todo
    template_name = "todoes/delete.html"
    success_url = "/todoes/"

    def get_queryset(self):
        usr = self.request.user
        return Todo.objects.filter(user=usr)
