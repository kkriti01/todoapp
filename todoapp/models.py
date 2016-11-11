from __future__ import unicode_literals

from django.db import models


class Todo(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=225, blank=True)
    low = '1'
    Medium = '2'
    High = '3'
    priority_choice = (
        (High, 'High'),
        (low, 'low'),
        (Medium, 'Medium'))
    state_task_choice = (
        ('todo', 'Todo'),
        ('doing', 'Doing'),
        ('done', 'Done'))
    priority = models.CharField(max_length=1, choices=priority_choice,default=Medium)
    state_task = models.CharField(max_length=10, choices=state_task_choice, default='todo')
    due_date = models.DateField()
