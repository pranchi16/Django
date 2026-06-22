from django.db import models

# Create your models here.

class Movie(models.Model):
    MOVIE_TYPES = [
        ('ACTION', 'Action'),
        ('COMEDY', 'Comedy'),
        ('DRAMA', 'Drama'),
        ('SCI-FI', 'Sci-Fi'),
        ('HORROR', 'Horror'),
    ]

    title = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    movie_type = models.CharField(max_length=20, choices=MOVIE_TYPES, default='ACTION')
    rating = models.IntegerField()

    def __str__(self):
        return self.title