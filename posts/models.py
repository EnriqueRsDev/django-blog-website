from django.db import models
from django.contrib.auth.models import User
from categories.models import Category
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50, blank=False)
    content = models.TextField(max_length=1000, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='posts')
    published = models.BooleanField(default=False)
    slug = models.SlugField(default='', null=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"