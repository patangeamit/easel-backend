from django.contrib import admin
from .models import Artist, Artwork, Comment, Essay

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin): pass

@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin): pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin): pass

@admin.register(Essay)
class EssayaAdmin(admin.ModelAdmin): pass