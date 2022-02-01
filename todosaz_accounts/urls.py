from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'accounts'

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('delete-account', views.del_account, name='del_account'),
    path('profile/', views.user_profile, name='profile'),
    path('change-pro-image/', views.change_profile_image, name='change_profile_image'),
    path('edit-profile/<int:pk>/', login_required(views.EditProfile.as_view()), name='edit_profile'),
    path('edit-about', views.edit_about, name='edit_about'),
    path('change-password/', views.SetPassword.as_view(), name='change_password'),
]
