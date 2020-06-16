from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Todo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    is_done = models.BooleanField(default=False)
    content = models.CharField(max_length=100)