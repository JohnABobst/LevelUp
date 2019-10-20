from django.db import models
from apps.user.models import User
# Create your models here.
class Goal(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    accomplished = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goals')

class Daily(models.Model):
    description = models.CharField(max_length=250)


    
