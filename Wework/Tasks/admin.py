from django.contrib import admin

# Register your models here.
from Tasks.models import Task

admin.site.register(Task)