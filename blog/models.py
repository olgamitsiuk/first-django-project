from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=100)  # Title of the book (up to 100 characters)
    published_date = models.DateField()  # Publication date of the book
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )

    def is_new_release(self):
        from datetime import date
        # Consider the book new if it was published within the last 10 year.
        return (date.today() - self.published_date).days <= 365*10

    def __str__(self):
        return f"{self.title} by {self.author}"
