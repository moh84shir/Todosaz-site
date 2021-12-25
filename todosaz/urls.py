from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("todoes/", include("todosaz_todoes.urls")),
    path("accounts/", include("todosaz_accounts.urls")),
    path("news/", include("todosaz_news.urls")),
    path("settings/", include("todosaz_settings.urls")),
    path("", include('todosaz_contact.urls')),
    path("admin/", admin.site.urls),
]
