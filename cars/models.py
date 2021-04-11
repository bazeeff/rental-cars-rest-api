from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from cars.UserManager import UserManager


class Car(models.Model):
    name = models.CharField(max_length=225)
    created_date = models.DateField()
    added_date = models.DateField()

    def __str__(self):
        return self.name

class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=255)
    email = models.EmailField(_('email address'), unique=True)
    cars = models.ManyToManyField('Car', related_name='users', blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
        #objects = UserManager()
    def __str__(self):
        return "{}".format(self.email)

