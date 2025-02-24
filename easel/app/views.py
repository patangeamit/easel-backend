from rest_framework import viewsets, filters
from .models import Artwork, Artist, Comment, Essay
from .serializers import ArtworkSerializer, ArtistSerializer, CommentSerializer, EssaySerializer
from rest_framework.permissions import IsAuthenticated, BasePermission
from user.models import UserTypeEnum
from django_filters.rest_framework import DjangoFilterBackend 
class AdminPerm(BasePermission):
    def has_permission(self, request, view):
        if not hasattr(request.user, "role"):
            return False
        if request.user.role == UserTypeEnum.ADMIN:
            return True
        return False
class AuthorPerm(BasePermission):
    def has_permission(self, request, view):
        if not hasattr(request.user, "role"):
            return False
        if request.user.role == UserTypeEnum.AUTHOR:
            return True
        return False
class ArtworkViewSet(viewsets.ModelViewSet):
    queryset = Artwork.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ArtworkSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]  # Enables sorting
    ordering_fields = ["id", "title", "artist", "date", "like_count"]  # Fields that can be sorted
    ordering = ["title"]  # Default sorting order
    filterset_fields = ["date", "movement", "artist"]
    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAuthenticated, AdminPerm]
        return super().get_permissions()
class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]  # Enables sorting
    ordering_fields = ["id", "name", "birth_date", "death_date", "nationality"]  # Fields that can be sorted
    ordering = ["name"]  # Default sorting order
    filterset_fields = ["nationality", "name"]
    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAuthenticated, AdminPerm]
        return super().get_permissions()

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class EssayViewSet(viewsets.ModelViewSet):
    queryset = Essay.objects.all()
    serializer_class = EssaySerializer
    def get_permissions(self):
        print(self.request.headers)
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAuthenticated, AuthorPerm]
        return super().get_permissions()

from django.shortcuts import render
from django.http import HttpResponse
from .models import Artwork

def artwork_list(request):
    artworks = Artwork.objects.all().order_by("-date")
    return render(request, "artworks/list.html", {"artworks": artworks})

def load_more_artworks(request):
    artworks = Artwork.objects.all().order_by("-date")[:5]  # Load 5 artworks
    return render(request, "artworks/partials/artworks.html", {"artworks": artworks})
