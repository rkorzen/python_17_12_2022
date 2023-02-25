from django.db import models

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, related_name="posts")
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = models.ManyToManyField("tags.Tag")

    def __str__(self): return f"{self.title}"