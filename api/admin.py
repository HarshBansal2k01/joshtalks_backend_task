from django.contrib import admin
from .models import User, Task, UserTask, StatusUpdate

admin.site.register(User)
admin.site.register(Task)
admin.site.register(UserTask)
admin.site.register(StatusUpdate)
