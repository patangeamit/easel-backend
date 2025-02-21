from rest_framework import serializers
from .models import Artwork, Artist, Comment, Essay

class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        fields = '__all__'
class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
class EssaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Essay
        fields = '__all__'