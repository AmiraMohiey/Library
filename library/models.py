from django.db import models

from django.contrib.auth.models import User

import os



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
    picture_url = models.ImageField(upload_to=os.path.join('library/static/images/author/%Y%m%d%H%M%S'),
                                    blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    published_at = models.DateField(null=True)
    country = models.CharField(null=True, max_length=100)
    link = models.URLField(null=True)
    picture_url = models.ImageField(upload_to=os.path.join('library/static/images/book/%Y%m%d%H%M%S'),
                                    blank=True, null=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
