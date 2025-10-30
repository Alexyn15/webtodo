from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    def get_queryset(self):
        queryset = Todo.objects.all()
        
        sort_by = self.request.query_params.get('sort_by', '-created_at')
        allowed_sorts = ['created_at', '-created_at', 'due_date', '-due_date', 'priority', '-priority', 'is_completed', '-is_completed']
        
        if sort_by in allowed_sorts:
            queryset = queryset.order_by(sort_by)
        
        return queryset
    
    @action(detail=True, methods=['patch'])
    def toggle_complete(self, request, pk=None):
        """Đánh dấu hoàn thành/chưa hoàn thành"""
        todo = self.get_object()
        todo.is_completed = not todo.is_completed
        todo.save()
        
        serializer = self.get_serializer(todo)
        return Response(serializer.data)