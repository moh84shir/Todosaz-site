from rest_framework.permissions import IsAdminUser
from todosaz_news.models import New
from todosaz_settings.models import Setting
from todosaz_todoes.models import Todo
from .serializers import TodoSerializer, NewSerializer, SettingSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# REST API FOR TODOES
class TodoListCreate(ListCreateAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


class TodoDetailUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


# REST API FOR NEWS
class NewListCreate(ListCreateAPIView):
    serializer_class = NewSerializer
    queryset = New.objects.all()


class NewDetailUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = New.objects.all()
    serializer_class = NewSerializer


# REST API FOR SETTINGS
class SettingListCreate(ListCreateAPIView):
    serializer_class = SettingSerializer
    queryset = Setting.objects.all()


class SettingDetailUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer
    permission_classes = [IsAdminUser]
