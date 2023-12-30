# todo_list/todo_app/serializers.py
from rest_framework import serializers
from .models import ToDoItem, ToDoList

class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = '__all__'

class ToDoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = '__all__'
