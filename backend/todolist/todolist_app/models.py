from django.db import models
from .validators import validate_list_name

# Create your models here.
class List(models.Model):
    list_name = models.CharField(
        max_length=255, null=False, blank=False, validators=[validate_list_name]
    )