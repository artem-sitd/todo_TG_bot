from django.urls import path
from .views import get_tasks_by_user, create_task

app_name = "tg_app"
urlpatterns = [
    path('tasks/<int:user_id>/', get_tasks_by_user, name='get_tasks'),
    path('tasks/create/', create_task, name='create_task'),
]
