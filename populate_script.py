import os, django, random
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "level_up.settings")
django.setup()
from apps.users.models import User 
from faker import Faker 
fake = Faker()

for user in User.objects.all():
    user.first_name= fake.first_name()
    user.last_name= fake.last_name()
    user.password = "123456789"
    user.email = fake.email() 
    user.birthday = birthday = fake.date_of_birth(minimum_age=18, maximum_age=115)  
    user.save()
