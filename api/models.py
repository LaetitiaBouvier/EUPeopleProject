from django.db import models
from django.core.validators import RegexValidator
import datetime
# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __unicode__(self):
        return "{0}".format(self.code, )

class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True) # validators should be a list

    email = models.EmailField(max_length=100)
    endofsubscription = models.DateField(default=datetime.date.today)

    def __unicode__(self):
        return '{0}'.format(self.code, )