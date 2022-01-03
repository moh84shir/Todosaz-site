from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('todo/todo-list/', views.TodoListCreate.as_view(), name="TodoCreateList"),
    path('todo/<int:pk>/', views.TodoDetailUpdateDelete.as_view(), name="TodoDetailUpdateDelete"),
    path('new/new-list/', views.NewListCreate.as_view(), name="NewCreateList"),
    path('new/<int:pk>/', views.NewDetailUpdateDelete.as_view(), name="NewDetailUpdateDelete"),
    path('settings/change/<int:pk>/', views.SettingDetailUpdateDelete.as_view(), name="SettingDetailUpdateDelete"),
]