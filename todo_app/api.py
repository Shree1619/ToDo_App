# todo_list/todo_app/api.py
from rest_framework import generics
from .models import ToDoItem, ToDoList
from .serializers import ToDoItemSerializer, ToDoListSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class TodoListAPIView(generics.ListCreateAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class TodoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
