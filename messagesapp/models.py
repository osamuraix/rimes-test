from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def count_letters(self):
        content = self.content.lower()
        return {
            'r': content.count('r'),
            'i': content.count('i'),
            'm': content.count('m'),
            'e': content.count('e'),
            's': content.count('s'),
        }

    def __str__(self):
        return f"Message from {self.user or 'Anonymous'}"