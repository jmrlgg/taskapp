from django.core import serializers
from rest_framework import exceptions, serializers
from .models import TaskModel

# RETRIEVE TASK PER FIELDS LISTED 
class TaskModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ('id', 'title', 'description', 'created_at', 'priority', 'due_date', 'tags', 'completed')

class Task2ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        template = ""
        fields = ('id', 'title', 'description', 'created_at', 'priority', 'due_date', 'tags', 'completed')



""" 
# TODO: Create Comments Table Allow to Call Comments Based on Task Model
class TasksSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=65)
    description = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField()
    priority = serializers.IntegerField()
    due_date = serializers.DateTimeField()
    tags = serializers.CharField(max_length=255, blank=True, null=True)
    completed = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return Tasks(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        return instance
    
        title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=255, blank=True, null=True)
    priority = models.CharField(max_length=255, blank=True, null=True)
    completed = models.BooleanField(default=False) 
"""
