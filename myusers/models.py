from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Base(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class UserGroup(Base):
    '''
    Model to Create Auth Group
    '''
    name = models.CharField(max_length=32, unique=True)

class User(AbstractUser, Base):
    '''
    Captures the User information
    '''
    display_name = models.CharField(max_length=32, db_index=True)