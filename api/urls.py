from django.urls import path
from .views import (
    UserListCreateView, TaskListCreateView, UserTaskCreateView,
    TasksForUserView, UsersForTaskView, StatusUpdateView
)

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('usertasks/', UserTaskCreateView.as_view(), name='user-task-create'),
    path('tasks-for-user/<int:user_id>/', TasksForUserView.as_view(), name='tasks-for-user'),
    path('users-for-task/<int:task_id>/', UsersForTaskView.as_view(), name='users-for-task'),
    path('status-update/', StatusUpdateView.as_view(), name='status-update'),
]
