import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Chirp(models.Model):

    author = models.ForeignKey(User)
    message = models.CharField(max_length=141)
    title = models.CharField(max_length=30, blank=True, null=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def is_recent(self):
        return timezone.now() - datetime.timedelta(days=1) <= self.posted_at

    def __str__(self):
        return "Author: {}, Message: {}, Posted at:{}".format(
            self.author.username, self.message, self.posted_at)


class Tag(models.Model):
    chirp = models.ManyToManyField(Chirp)
    name = models.CharField(max_length=15)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Name: {} Posted At: {}".format(self.name, self.posted_at)
