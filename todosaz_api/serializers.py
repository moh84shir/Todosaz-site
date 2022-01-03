from rest_framework import serializers
from todosaz_todoes.models import Todo
from todosaz_news.models import New
from todosaz_settings.models import Setting
from rest_framework.permissions import IsAdminUser


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = "__all__"


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = "__all__"
