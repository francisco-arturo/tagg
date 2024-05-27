from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Playlist(models.Model):
    title = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name="playlists", blank=True)
    cover_art_url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Song(models.Model):
    title = models.CharField(max_length=150)
    artist = models.CharField(max_length=255, blank=True)
    album = models.CharField(max_length=150, blank=True)
    release_date = models.DateField(null=True, blank=True)
    genre = models.CharField(max_length=20, blank=True)
    duration = models.IntegerField(blank=True, null=True)
    cover_art_url = models.URLField(blank=True)
    play_count = models.IntegerField(default=0)
    added_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name="songs", blank=True)
    playlists = models.ManyToManyField(Playlist, related_name="songs", blank=True)

    def __str__(self):
        return self.title
