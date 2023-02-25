from django.db import models
from common.models import Timestamped

# Create your models here.





class Post(Timestamped):
    author = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, related_name="posts")
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = models.ManyToManyField("tags.Tag", related_name="posts", blank=True)

    def __str__(self): return f"{self.title}"

    # class Meta:
    #     verbose_name_plural = "renifer"
