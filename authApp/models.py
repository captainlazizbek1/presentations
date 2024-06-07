from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, AbstractUser
from uuid import uuid4
from random import randint

# Create your models here.

def id_generator():
    id = ''
    for i in range(3):
        num = randint(100,1000)
        id = id + str(num)
    return int(id)


class User(AbstractUser):
    id = models.CharField(primary_key=True, unique=True, default=id_generator)



            