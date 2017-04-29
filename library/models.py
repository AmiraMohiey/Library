from django.db import models
import os
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    picture_url = models.CharField(max_length=100)
    users = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    born_at = models.DateField(null=True)
    died_at = models.DateField(null=True)
    website = models.CharField(null=True, max_length=100)
    bio = models.TextField(null=True)
    picture_url = models.ImageField(upload_to=os.path.join('author/%Y%m%d%H%M%S'),

                                    blank=True, null=True)

    users = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    published_at = models.DateField(null=True)
    country = models.CharField(null=True, max_length=100)
    link = models.URLField(null=True)

    picture_url = models.ImageField(upload_to=os.path.join('book/%Y%m%d%H%M%S'),

                                    blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, through='UserBookRelation')

    @property
    def rate(self):
        try:
            return int(self.userbookrelation_set.filter(rate__gt=0).aggregate(Avg('rate'))['rate__avg']*20)
        except :
            return 0

    def stared(self):
        try:
            return self.userbookrelation_set.filter(rate__gt=0).aggregate(Avg('rate'))['rate__avg']
        except :
            return 0


    @property
    def rate_count(self):
        try:
            return self.userbookrelation_set.filter(rate__gt=0).count()
        except:
            return 0


    def __str__(self):
        return self.title


class UserBookRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    wish = models.BooleanField(default=False)
    read = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'book',)
