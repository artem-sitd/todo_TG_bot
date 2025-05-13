from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('message', 'user_id', 'created_at')
    list_filter = ('user_id',)
    search_fields = ('message', 'tag', 'user_id')
