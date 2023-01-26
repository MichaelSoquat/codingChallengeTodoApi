from django.db import models
import datetime

# Create your models here.
priority_choices = [('Low', 'Low'), ('Medium', 'Medium'), ('Urgent', 'Urgent')]

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    creation_date = models.DateField(default = datetime.date.today)
    priority = models.CharField(max_length=10, choices=priority_choices, default='Low')


    def __str__(self):
        return self.title
