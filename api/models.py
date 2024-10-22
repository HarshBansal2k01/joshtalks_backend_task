from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'mobile']

    def __str__(self):
        return self.email

class Task(models.Model):
    STATUS_PENDING = 'Pending'  
    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),  
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task_type = models.CharField(max_length=50)  
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class UserTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='Assigned')  
    assigned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.name} -> {self.task.name}'

class StatusUpdate(models.Model):
    STATUS_COMPLETE = 'Completed'  
    STATUS_CHOICES = [
        (STATUS_COMPLETE, 'Completed'),  
    ]  
    user_task = models.ForeignKey(UserTask, on_delete=models.CASCADE)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES, default=STATUS_COMPLETE ) 
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'Status update for {self.user_task}'
