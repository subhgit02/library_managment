from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Author(Models.Model):
    name= models.CharField(max_length=255)
    birthday = models.DateField()
    biography = models.TextField(blank = True, null = True)


def _str_(self):
    return self.name
class Country(models.Model):
    name= models.CharField(max_length=255)
    code = models.CharField(max_length=2, unique = True)

def _str_(self):
    return self.name

class Book(models.Model):
    title= models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    published_date = models.DateField()
    ishn = models.CharField(max_length=13, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    owner = models.ForeignKey(User, on_delete = models.CASCADE)

def _str_(self):
    return self.name

class BookCountry(models.Model):
    AVAILABLE = 'available'
    OUT_OF_STOCK = 'out of stock'
    PRE_ORDER = 'pre-order'
    STATUS_CHOISES = [
        (AVAILABLE, 'available'),
    (OUT_OF_STOCK,'out of stock'),
    (PRE_ORDER,'pre-order')
    ]
book = models.ForeignKey(Book, on_delete = models.CASCADE)
country = models.ForeignKey(Country, on_delete = models.CASCADE)
available_status = models.Charfeild(max_length = 20, choices = STATUS_CHOICES)
release_date = models.DateField()

class Meta:
    unique_togather = ('book','country')

