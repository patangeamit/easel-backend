from django.db import models
from user.models import User
class Artist(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField(blank=True, null=True)
    death_date = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.nationality})"

class Artwork(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/artworks/')
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True, related_name='artworks')
    date = models.DateField()
    location = models.CharField(max_length=255, blank=True, null=True)
    like_count = models.PositiveIntegerField(default=0)
    movement = models.CharField(max_length=255, default="")
    def __str__(self):
        return self.title

class Essay(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='essays')
    artwork = models.ForeignKey(Artwork, on_delete=models.SET_NULL, null=True, related_name='essays')
    references = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Essay on {self.artwork.title} by {self.author.username}'

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comments')
    artwork = models.ForeignKey(Artwork, on_delete=models.SET_NULL,null=True, related_name='comments')
    content = models.TextField()
    like_count = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.artwork.title}'
