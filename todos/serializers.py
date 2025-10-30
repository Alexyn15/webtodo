from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'is_completed', 'priority', 'due_date', 'created_at']
        read_only_fields = ['created_at']