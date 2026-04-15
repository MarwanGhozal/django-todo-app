from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'description', 'created_at', 'updated_at')
    search_fields = ('user', 'title')


admin.site.register(Task, TaskAdmin)
