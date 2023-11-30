from django.db import models

# Create your models here.
class List(models.Model):
    list_name = models.CharField(
        max_length=255, null=False, blank=False, validators=[validate_list_name]
    )