from rest_framework import serializers
from todosaz_todoes.models import Todo
# Create your serializers here.


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"