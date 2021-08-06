from django.db import models


# Create your models here.
class Movie(models.Model):
    imdb_id = models.CharField(max_length=48, null=False)
    genres = models.CharField(max_length=200, null=True)
    original_title = models.CharField(max_length=500, null=False)
    overview = models.TextField(max_length=500, null=True)
    vote_average = models.FloatField(default=0)
    poster_path = models.CharField(max_length=64, null=True)
