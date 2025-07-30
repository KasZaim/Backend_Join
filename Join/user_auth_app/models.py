from django.db import models
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    initials = models.CharField(max_length=2, null=True, blank=True)
    color = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.user.username