from django.db import models
import os

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    date_added = models.DateField(auto_now=True)
    video_file = models.FileField(upload_to="movies/")
    thumbnail = models.ImageField(upload_to="thumbnails/")

    def delete(self, *args, **kwargs):
        if self.video_file:
            if os.path.isfile(self.video_file.path):
                os.remove(self.video_file.path)

        if self.thumbnail:
            if os.path.isfile(self.thumbnail.path):
                os.remove(self.thumbnail.path)

        super().delete(*args, **kwargs)