from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    picture_url = models.CharField(max_length=100)

    def __str__(self):
        return self.name
