from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('todo/todo-list/', views.TodoListCreate.as_view(), name="todo_create_list"),
    path('todo/<int:pk>/', views.TodoDetailUpdateDelete.as_view(), name="todo_detail_update_delete"),
    path('new/new-list/', views.NewListCreate.as_view(), name="new_create_list"),
    path('new/<int:pk>/', views.NewDetailUpdateDelete.as_view(), name="new_detail_update_delete"),
    path('settings/change/<int:pk>/', views.SettingDetailUpdateDelete.as_view(), name="settings_detail_update_delete"),
    path('accounts/login/', views.user_login, name="login"),
    path('accounts/register/', views.register, name="register"),
    path('accounts/logout/', views.user_logout, name="logout"),
]