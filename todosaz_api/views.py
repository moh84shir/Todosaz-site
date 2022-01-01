from rest_framework.decorators import api_view
from rest_framework.response import Response
from todosaz_todoes.models import Todo
from .serializers import TodoSerializer

# Create your views here.


@api_view(['GET'])
def todo_list(request):
    todoes = Todo.objects.all()
    todoes_serializer = TodoSerializer(instance=todoes, many=True)
    return Response(todoes_serializer.data)
