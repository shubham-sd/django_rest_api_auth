from django.db import models

# Create your models here.
class Base(models.Model):
    '''
    Base Model for all retest_app models
    '''
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Employee(Base):
    '''
    Employee Model
    '''
    name = models.CharField(max_length=32, db_index=True)
    id_number = models.IntegerField(unique=True, null=False, db_index=True)
    date_of_joining = models.DateField()
    salary = models.FloatField(null=True)
    active = models.BooleanField(default=True)