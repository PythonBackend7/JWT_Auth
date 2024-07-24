# tasks/models.py

from django.db import models
from accounts.models import CustomUser


class Task(models.Model):
    title = models.CharField(max_length=212)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
