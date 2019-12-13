from django.db import models
from apps.users.models import User

class Goal(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    accomplished = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goals')

class Daily(models.Model):
    description = models.CharField(max_length=250)
    goal = models.ForeignKey(Goal ,on_delete=models.CASCADE, related_name='dailies')
    accomplished = models.BooleanField(default=False)

class Weekly(models.Model):
    description = models.CharField(max_length=255)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='weeklies')
    accomplished = models.BooleanField(default=False)

class Benchmark(models.Model):
    description = models.CharField(max_length=255)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='benchmarks')
    accomplished = models.BooleanField(default=False)




    
