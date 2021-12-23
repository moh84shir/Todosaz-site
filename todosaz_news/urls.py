from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = "news"

urlpatterns = [
    path("", login_required(views.NewsList.as_view()), name="news_list"),
    path("<int:pk>/", views.new_detail, name="new_detail"),
    path("create/", views.create_new, name="create_new"),
    path("delete/<int:pk>/", views.delete_new, name="delete_new"),
    path("edit/<int:pk>/", login_required(views.UpdateNew.as_view()), name="edit_new"),
]
