from django.db import models
import datetime
from django.conf import settings

state_choices = [('To Do', 'To Do'), ('In Progress', 'In Progress'), ('Done', 'Done')]
priority_choices = [('Low', 'Low'), ('Medium', 'Medium'), ('Urgent', 'Urgent')]

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    state = models.CharField(max_length = 17, choices = state_choices, default = 'To Do')
    creation_date = models.DateField(default = datetime.date.today )
    priority = models.CharField(max_length=10, choices=priority_choices, default='Low')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = 'creator')


    def __str__(self):
        return self.title



