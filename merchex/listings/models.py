from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5, null=True)
    biography = models.CharField(max_length=1000, null=True)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2025)],
        null=True
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    
class Listing(models.Model):
    title = models.fields.CharField(max_length=100)
   
