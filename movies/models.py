from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=30, null=False)
    gender = models.CharField(max_length=30, null=False)
    director = models.CharField(max_length=30, null=False)
    release_year = models.CharField(max_length=30, null=False)
    synopsis = models.CharField(max_length=400, null=False)
    
    def __str__(self):
        return f'{self.title} - {self.gender}'

