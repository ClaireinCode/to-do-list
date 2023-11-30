from django.db import models
from .models import List

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(
        blank=False
    )
    completed = models.BooleanField (
        default=False
    )
    parent_list = models.ManyToOneRel(List)

    