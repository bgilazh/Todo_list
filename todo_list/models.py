from django.db import models

# Create your models here.

class Todo(models.Model):
    note = models.CharField(max_length=1000)

    