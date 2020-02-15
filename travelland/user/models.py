from datetime import date

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=30, blank=True)
    contact = models.IntegerField(blank=True)
    address = models.CharField(max_length=30, blank=True)
    guider = models.CharField(max_length=30, blank=True)

def __str__(self):
    return self.contact


class Post(models.Model):
    user_name = models.CharField(max_length=25)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    blog_pic = models.ImageField(upload_to="photos/blog", blank=True)
    date = models.DateTimeField(auto_now=True)


def __str__(self):
    return self.title
