from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL #'auth.User'

class Car(models.Model):
    #user = models.ForeignKey(User)
    #driver = models.ManyToManyField(User)
    updated_by = models.ForeignKey(User, related_name='updated_car_user', null=True, blank=True)
    first_owner = models.OneToOneField(User)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


