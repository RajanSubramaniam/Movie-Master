from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator


# Create your models here.
class Movie(models.Model):
	title = models.CharField(max_length=255)
	genre = models.CharField(max_length=255)
	description = models.TextField()
	user_ratings = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
	slug = models.SlugField(unique=True)
