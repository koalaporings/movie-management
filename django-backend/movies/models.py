from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    date_added = models.DateField(auto_now=True)
    video_file = models.FileField(upload_to="movies/")
    thumbnail = models.ImageField(upload_to="thumbnails/")