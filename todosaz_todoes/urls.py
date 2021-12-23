from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = "todoes"

urlpatterns = [
    path("", login_required(views.TodoList.as_view()), name="todo_list"),
    path("<int:pk>/", login_required(views.TodoDetail.as_view()), name="todo_detail"),
    path("create/", login_required(views.CreateTodo.as_view()), name="create_todo"),
    path(
        "edit/<int:pk>/",
        login_required(views.UpdateTodo.as_view()),
        name="edit_todo",
    ),
    path(
        "delete/<int:pk>/",
        login_required(views.DeleteTodo.as_view()),
        name="delete_todo",
    ),
]
