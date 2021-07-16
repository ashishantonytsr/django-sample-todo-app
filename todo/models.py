from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length = 120, null=False)
    description = models.TextField(null=True)
    date_of_execution = models.DateField()
