from rest_framework import serializers
from .models import User, Task, UserTask, StatusUpdate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email','mobile']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'created_at', 'task_type', 'status', 'completed_at']

class UserTaskSerializer(serializers.ModelSerializer):
   
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())  # Displays user dropdown
    task = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all())  # Displays task dropdown
    status = serializers.CharField()  # This ensures the status is reflected correctly

    class Meta:
        model = UserTask
        fields = ['id', 'user', 'task', 'status', 'assigned_at']


class StatusUpdateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)  # Dropdown for users
    task = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all(), write_only=True)  # Dropdown for tasks based on the user selected

    class Meta:
        model = StatusUpdate
        fields = ['id', 'user', 'task', 'status', 'updated_at', 'completed_at']

    def validate(self, data):
        user = data.get('user')
        task = data.get('task')

        # Ensure the task is assigned to the selected user
        if not UserTask.objects.filter(user=user, task=task).exists():
            raise serializers.ValidationError('This task is not assigned to the selected user.')

        return data

    def create(self, validated_data):
        # Retrieve the existing UserTask and update the status
        user_task = UserTask.objects.get(user=validated_data['user'], task=validated_data['task'])
        
        status_update = StatusUpdate.objects.create(
            user_task=user_task,
            status=validated_data['status'],
            completed_at=validated_data.get('completed_at')
        )

        return status_update
