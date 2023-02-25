from django.db import models
from django.utils.timezone import now, timedelta


# Create your models here.

class CheckAgeMixin:

    def is_older_than(self, days=1):
        delta = timedelta(days=days)
        return (now() - self.created) > delta


class Timestamped(models.Model, CheckAgeMixin):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(Timestamped):
    author = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, related_name="posts")
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = models.ManyToManyField("tags.Tag", related_name="posts", blank=True)

    def __str__(self): return f"{self.title}"

    # class Meta:
    #     verbose_name_plural = "renifer"
