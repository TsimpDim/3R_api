from django.core.exceptions import ValidationError

def validate_no_duplicates(value):
    if len(set(value)) != len(value): raise ValidationError('Tags contain duplicates.')