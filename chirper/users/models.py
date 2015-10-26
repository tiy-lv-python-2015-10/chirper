from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

def validate_age(age):
    if 18 > age or 50 < age:
        raise ValidationError("Age not allowed")

class Profile(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'
    GENDER_CHOICES = (
        (MALE, 'Man'),
        (FEMALE, 'Woman'),
        (OTHER, 'Complicated')
    )

    user = models.OneToOneField(User)
    age = models.IntegerField(validators=[validate_age])
    gender = models.CharField(max_length=8, choices=GENDER_CHOICES,
                              default=MALE)

    def __str__(self):
        return "{} Age: {} Gender: {}".format(self.user.username, self.age,
                                              self.gender)