from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_rating(value):
    if value < 0 or value > 10 :
        raise ValidationError(
            _('Rating must be from 0-10'),
            params={'value': value},
        )

# Create your models here.

class Visit(models.Model):
    id =  models.BigAutoField(auto_created = True, primary_key = True, null=False)
    name = models.CharField(max_length=50, null=False)
    place = models.CharField(max_length=100, null=False)
    time = models.TimeField(auto_now=False, auto_now_add=False, null=False)
    date = models.DateField(auto_now=False, auto_now_add=False, null=False)
    description = models.CharField(max_length=300, null=False)
    rating = models.IntegerField(validators=[validate_rating], null=False)