from django.db import models
# blog/models.py

from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)  # optional image
    thumbnail = models.ImageField(
    upload_to='thumbnails/',
    blank=True,
    null=True,
    default='thumbnails/default.webp'
)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Create your models here.
