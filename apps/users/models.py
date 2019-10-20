from django.db import models
from datetime import datetime, timedelta
import re 
# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        name_regex = re.compile(r'^[a-zA-Z]+$')
        if datetime.strptime(postData['birthday'],'%Y-%m-%d') > datetime.now() - timedelta(days=13*365):
            errors['birthday'] = 'You must be at least 13 years old to join'
        if len(postData['first_name']) < 3:
            errors['first_name'] = 'First name must be longer than 2 characters'
        if len(postData['last_name']) < 3:
            errors['last_name'] = 'Last name must be longer than 2 characters'
        if not name_regex.match(postData['first_name']):
            errors['first_name_characters'] = "A name can only contain letters"
        if not name_regex.match(postData['last_name']):
            errors['last_name_characters'] = "A name can only contain letters"
        email_regex = re.compile(r'^[a-zA-Z0-9+_-]+@[a-zA-Z0-9+_-]+\.[a-zA-Z0-9+]')
        if not email_regex.match(postData['email']):
            errors['email'] = 'Invalid email format'
        if postData['email'] in [user.email for user in User.objects.all()]:
            errors['email_taken'] = 'There is already an account using that email'
        if postData['password'] != postData['confirm_password']:
            errors['password'] = "Passwords don't match"
        if len(postData['password']) < 8:
            errors['password_length'] = "Password must be at least 8 characters long"

        return errors



class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    birthday = models.DateField()
    objects = UserManager()
    xp = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    next_level = models.IntegerField(default=100)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"



