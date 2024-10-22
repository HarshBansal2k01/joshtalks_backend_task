from rest_framework import generics
from .models import User, Task, UserTask, StatusUpdate
from .serializers import UserSerializer, TaskSerializer, UserTaskSerializer, StatusUpdateSerializer
from rest_framework.response import Response
from rest_framework import status

# Create or List Users
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Create or List Tasks
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Create UserTask (Assign Task to Users)
class UserTaskCreateView(generics.CreateAPIView):
    queryset = UserTask.objects.all()
    serializer_class = UserTaskSerializer

# Retrieve tasks assigned to a specific user
class TasksForUserView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        user_tasks = UserTask.objects.filter(user_id=user_id).values_list('task_id', flat=True)
        return Task.objects.filter(id__in=user_tasks)

# Retrieve users assigned to a specific task
class UsersForTaskView(generics.ListAPIView):
    serializer_class = UserTaskSerializer

    def get_queryset(self):
        task_id = self.kwargs['task_id']
        return UserTask.objects.filter(task_id=task_id)

# Update task status for a specific user-task relationship
class StatusUpdateView(generics.CreateAPIView):
    queryset = StatusUpdate.objects.all()
    serializer_class = StatusUpdateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


