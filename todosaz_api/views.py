from rest_framework.permissions import IsAdminUser, IsAuthenticated
from todosaz_news.models import New
from todosaz_settings.models import Setting
from todosaz_todoes.models import Todo
from .serializers import TodoSerializer, NewSerializer, SettingSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsAdminUserOrReadOnly


# REST API FOR TODOES
class TodoListCreate(ListCreateAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    permission_classes = ((IsAuthenticated,))


class TodoDetailUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = ((IsAuthenticated,))


# REST API FOR NEWS
class NewListCreate(ListCreateAPIView):
    serializer_class = NewSerializer
    queryset = New.objects.all()
    permission_classes = ((IsAdminUserOrReadOnly,))


class NewDetailUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = New.objects.all()
    serializer_class = NewSerializer
    permission_classes = ((IsAdminUserOrReadOnly,))


# REST API FOR SETTINGS
class SettingListCreate(ListCreateAPIView):
    serializer_class = SettingSerializer
    queryset = Setting.objects.all()
    permission_classes = ((IsAdminUser,))


class SettingDetailUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer
    permission_classes = ((IsAdminUser,))
