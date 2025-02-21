from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtworkViewSet, ArtistViewSet, CommentViewSet, EssayViewSet

router = DefaultRouter()
router.register(r'artworks', ArtworkViewSet, basename="artworks")
router.register(r'artists', ArtistViewSet, basename="artists")
router.register(r'comments', CommentViewSet, basename="comments")
router.register(r'essays', EssayViewSet, basename="essays")
urlpatterns = [
    path('', include(router.urls)),
]