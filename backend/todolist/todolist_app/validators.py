from django.core.exceptions import ValidationError
import re

def validate_list_name(value):
    name_pattern = re.compile(r'^[A-Za-z]+')
    if not name_pattern.match(value):
        raise ValidationError('Name must be in the format "Name"')
