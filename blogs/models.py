from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    CATEGORY_CHOICES = [
        ('article', 'Article'),
        ('news', 'News'),
    ]

    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='articles/', null=True, blank=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title