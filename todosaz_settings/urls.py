from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = "settings"

urlpatterns = [
    path("change/", views.change_settings, name="change_settings"),
    path("rest/", views.rest_settings, name="rest_settings"),
]
