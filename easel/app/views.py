from rest_framework import viewsets
from .models import Artwork, Artist, Comment, Essay
from .serializers import ArtworkSerializer, ArtistSerializer, CommentSerializer, EssaySerializer
from rest_framework.permissions import IsAuthenticated, BasePermission
from user.models import UserTypeEnum
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
    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAuthenticated, AdminPerm]
        return super().get_permissions()
class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
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
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAuthenticated, AuthorPerm]
        return super().get_permissions()