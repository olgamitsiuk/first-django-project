from django.contrib import admin

from .models import Author  # Replace with your model name
from .models import Book

admin.site.register(Author)
admin.site.register(Book)
