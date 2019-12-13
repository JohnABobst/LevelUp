import os, django, random
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "level_up.settings")
django.setup()
from apps.users.models import User 
from faker import Faker 
fake = Faker()

# for i in range(10):
#     User.objects.create(
#         first_name= fake.first_name(),
#         last_name= fake.last_name(),
#         username = fake.user_name(),
#         password = "123456789",
#         email = fake.email(),
#         birthday = fake.date_of_birth(minimum_age=18, maximum_age=115) 
# )

    

