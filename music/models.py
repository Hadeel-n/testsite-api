from django.db import models

# Create your models here.
class Album(models.Model):
    album_title = models.CharField(max_length=500)
    artist = models.CharField(max_length=250)

    def __str__(self):
      return self.album_title+" "+self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title=models.CharField(max_length=250)

    def __str__(self):
       return self.song_title