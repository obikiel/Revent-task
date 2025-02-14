from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, task_count

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task') 

urlpatterns = [
    path('', include(router.urls)),
    path('task-count/', task_count),
]
