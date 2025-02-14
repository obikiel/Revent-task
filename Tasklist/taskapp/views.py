from rest_framework import viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    """ViewSet for managing tasks."""
    queryset = Task.objects.all().order_by('-created_at')  # ✅ Ensure queryset is defined
    serializer_class = TaskSerializer

    @action(detail=True, methods=['patch'])
    def mark_complete(self, request, pk=None):
        """Mark a specific task as completed."""
        task = get_object_or_404(Task, pk=pk)
        task.completed = True
        task.save()
        return Response({'status': 'Task marked as completed'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def completed_tasks(self, request):
        """Retrieve all completed tasks."""
        completed_tasks = Task.objects.filter(completed=True)
        serializer = self.get_serializer(completed_tasks, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def task_count(request):
    """Retrieve the total count of tasks."""
    total_tasks = Task.objects.count()
    completed_tasks = Task.objects.filter(completed=True).count()
    return Response({
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': total_tasks - completed_tasks
    })
