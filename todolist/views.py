from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import path
from django.db import models
from models import Task

def task_list(request):
    tasks = Task.objects.all()  # Retrieve all posts from the database
    return HttpResponse(f"List of tasks: {tasks}")  # Return a simple HttpResponse for demonstration
    # return render(request, 'blog/post_list.html', {'posts': posts})

# Now, let's create a view to display the details of a specific blog post based on its ID.
def task_detail(request, id):
    task = get_object_or_404(Task, pk=id)  # Fetch the Task by ID or return a 404 error if not found
    return HttpResponse(f"Task Detail: {task}")  # Return a simple HttpResponse for demonstration
    # return render(request, 'blog/post_detail.html', {'post': post})

# Create a view to delete a specific blog post based on its ID.
def task_delete(request, id):
    task = get_object_or_404(Task, pk=id)  # Fetch the post by ID or return a 404 error if not found
    if request.method == 'POST':
        task.delete()  # Delete the post from the database
        return redirect('task_list')  # Redirect to the list of posts after deletion
    return HttpResponse(f"Task Delete: {task}")  # Return a simple HttpResponse for demonstration
    # return render(request, 'blog/post_confirm_delete.html', {'post': post})
