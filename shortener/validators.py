from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validate_url(value):
    url_validator = URLValidator()
    bool1 = False
    bool2 = False
    try:
        url_validator(value)
    except:
        bool1 = True
    http_plus_url = "https://" + value
    try:
        url_validator(http_plus_url)
    except:
        bool2 = True
    if bool1 and bool2:
        raise ValidationError("This url is not valid")
    return value

def validate_dot_com(value):
    if not "com" in value:
        raise ValidationError(".com is absent")
    return value