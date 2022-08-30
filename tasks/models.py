from turtle import title
from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100, default="Some String")
    description = models.TextField(blank=True)