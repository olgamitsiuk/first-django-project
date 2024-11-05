from django.urls import path
from .views import * 


app_name = 'todolist'  # Defining the namespace

urlpatterns = [
    path('', task_list, name='task_list'),  # URL for the list of posts
    path('task/<int:id>/', task_detail, name='task_detail'),  # URL for a specific post
    path('task/<int:id>/delete/', task_delete, name='task_delete')  # URL for deleting a specific post
]