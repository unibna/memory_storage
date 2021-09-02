from django.contrib.gis import views
from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string

from django.contrib.auth.models import User
from django.contrib.gis.db.models import PointField


class Memory(models.Model):
    name = models.CharField(max_length=128)
    location = PointField(null=True)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} - {self.name}"