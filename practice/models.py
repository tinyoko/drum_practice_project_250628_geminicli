from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=200)
    audio_file = models.FileField(upload_to='songs/')

    def __str__(self):
        return self.title

class Score(models.Model):
    song = models.OneToOneField(Song, on_delete=models.CASCADE)
    pdf_file = models.FileField(upload_to='scores/')
    page_timings = models.JSONField(default=list)

    def __str__(self):
        return f"Score for {self.song.title}"