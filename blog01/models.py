from typing import Iterable
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.TextField(max_length=10000, default="No description available")
    image = models.ImageField(upload_to="blogPostImages/%Y/%m/%d", blank=True, null=True)
    tag = models.CharField(max_length=25)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} - {self.tag}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)

            if img.height > 580 or img.width > 533:
                img.thumbnail((580, 533))
                img.save(self.image.path)
