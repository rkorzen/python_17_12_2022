from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=200)
    year = models.SmallIntegerField()

    def __str__(self):
        return f"{self.title} ({self.author})"