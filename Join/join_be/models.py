from django.db import models
from django.contrib.auth.models import User


class Contacts(models.Model):
    user = models.ForeignKey(User, related_name='contacts', on_delete=models.CASCADE, null=True, blank=False)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=100, blank=True )
    mail = models.CharField(max_length=50)
    phone = models.CharField(max_length=16) 
    initials = models.CharField(max_length=2)
    color = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Tasks(models.Model):
    category = models.CharField(max_length=20)
    topic = models.IntegerField(blank=False, null=True, default=0)
    headline = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    clients = models.ManyToManyField(Contacts, related_name="assigned_tasks", blank=True)
    date = models.DateField(null=True, blank=True)
    prio = models.CharField(max_length=50)
    subtasks = models.JSONField(default=list, null=True, blank=True, help_text="status: toDo, inProgress, awaitingFeedback, done")
    
    def __str__(self):
        return self.headline
