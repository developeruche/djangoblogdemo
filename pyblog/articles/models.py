from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default="default.png", blank=True)
    author = models.ForeignKey(
        User, default=None, on_delete=models.SET_NULL,  null=True)

    def __str__(self):
        return self.title

    def snippet(self):
        if(len(self.body) > 50):
            to_display = self.body[:50] + "..."
            return to_display
        else:
            to_display = self.body[:50]
            return to_display
