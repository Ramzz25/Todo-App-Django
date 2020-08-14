from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
import datetime

# Create your models here.

class todo_item(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.user.username
