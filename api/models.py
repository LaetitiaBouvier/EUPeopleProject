from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
import datetime
# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __unicode__(self):
        return "{0}".format(self.code, )

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True) # validators should be a list

    email = models.EmailField(max_length=100)
    endofsubscription = models.DateField(default=datetime.date.today)
    image = models.ImageField(default='../user.png')

    def __unicode__(self):
        return '{0}'.format(self.code, )

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Book(models.Model):
    author = models.ForeignKey(Author, related_name='book')
    title = models.CharField(max_length=255)
    edition = models.CharField(max_length=255)
    release_date = models.DateField(default=datetime.date.today)
    number_of_page = models.IntegerField(default=0)
    langage = models.CharField(max_length=255)
    isnb = models.CharField(max_length=255)
    image = models.ImageField(default='../users.png')
    category = models.CharField(max_length=255)

    def __str__(self):
        return "%s" % self.title

class Rent(models.Model):
    book = models.ForeignKey(Book, related_name='rent')
    member = models.ForeignKey(User, related_name='rent')
    renting_date = models.DateField(default=datetime.date.today)
    returning_date = models.DateField(default=datetime.date.today)
    returned = models.BooleanField(default=False)