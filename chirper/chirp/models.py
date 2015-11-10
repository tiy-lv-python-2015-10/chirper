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
    image = models.ImageField(upload_to='chirp_images', blank=True, null=True)

    def is_recent(self):
        recent = False
        yesterday = timezone.now() - datetime.timedelta(days=1)
        if yesterday <= self.posted_at:
            recent = True

        return recent

    def get_tag_count(self):
        return len(self.tag_set.all())

    def __str__(self):
        return "Author: {}, Message: {}, Posted at:{}".format(
            self.author.username, self.message, self.posted_at)

    def __repr__(self):
        return self.__str__()

    class Meta:
        ordering = ['-posted_at']


class Tag(models.Model):
    chirp = models.ManyToManyField(Chirp)
    name = models.CharField(max_length=15)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Name: {} Posted At: {}".format(self.name, self.posted_at)
