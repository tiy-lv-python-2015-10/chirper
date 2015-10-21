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
