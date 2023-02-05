from django.db import models

class Todo(models.Model):
    title = models.CharField(verbose_name="Tytuł", max_length=255)
    description = models.TextField(verbose_name="Opis")
    done = models.BooleanField(default=False)