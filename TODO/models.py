from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todo(models.Model):
    STATUS = [
        ('pending','pending'),
        ('completed','completed'),
    ]

    user = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=200,choices=STATUS)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
