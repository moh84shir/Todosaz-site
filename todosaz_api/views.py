from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from todosaz_news.models import New
from todosaz_settings.models import Setting
from todosaz_todoes.models import Todo

from .permissions import IsAdminUserOrReadOnly
from .serializers import (NewSerializer, SettingSerializer, TodoSerializer,
                          UserSerializer)


class TodoListCreate(ListCreateAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    permission_classes = (IsAuthenticated,)


class TodoDetailUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)


class NewListCreate(ListCreateAPIView):
    serializer_class = NewSerializer
    queryset = New.objects.all()
    permission_classes = (IsAdminUserOrReadOnly,)


class NewDetailUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = New.objects.all()
    serializer_class = NewSerializer
    permission_classes = (IsAdminUserOrReadOnly,)


class SettingListCreate(ListCreateAPIView):
    serializer_class = SettingSerializer
    queryset = Setting.objects.all()
    permission_classes = (IsAdminUser,)


class SettingDetailUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer
    permission_classes = (IsAdminUser,)


@api_view(["POST"])
def user_login(request):
    if not request.user:
        if request.method == "POST":
            data = request.data
            username = data.get("username")
            password = data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
def register(request):
    if not request.user:
        if request.method == "POST":
            serializer = UserSerializer(data=request.data)
            data = {}
            if serializer.is_valid():
                user = serializer.save()
                data["user"] = user
                data["token"] = Token.objects.get(user=user).key
            else:
                data["message"] = "عملیات با شکست مواجه شد"
            return Response(data=data)
    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def user_logout(request):
    if request.user:
        user_token = Token.objects.get(user=request.user)
        user_token.delete()
        logout(request)
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)
