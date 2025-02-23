from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from user.models import UserTypeEnum
from .models import Artwork, Artist, Comment, Essay
from django.core.files.uploadedfile import SimpleUploadedFile

User = get_user_model()

class ViewSetTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create users
        self.admin_user = User.objects.create_user(username="admin", password="adminpass", role=UserTypeEnum.ADMIN)
        self.author_user = User.objects.create_user(username="author", password="authorpass", role=UserTypeEnum.AUTHOR)
        self.end_user = User.objects.create_user(username="enduser", password="userpass", role=UserTypeEnum.EUSER)

        # Create sample data
        self.artist = Artist.objects.create(name="Test Artist", nationality="Testland")
        self.artwork = Artwork.objects.create(
            title="Test Artwork",
            artist=self.artist,
            date="2023-01-01",
            location="Test Museum",
            movement="Test Movement"
        )
        self.essay = Essay.objects.create(
            title="Test Essay",
            content="Essay Content",
            author=self.author_user,
            artwork=self.artwork
        )
        self.comment = Comment.objects.create(
            user=self.end_user,
            artwork=self.artwork,
            content="Test Comment"
        )

    # --- ARTIST TESTS ---

    def test_admin_can_create_artist(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.post("/api/artists/", {"name": "New Artist", "nationality": "Newland"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_can_get_artists(self):
        self.client.force_authenticate(user=self.end_user)
        response = self.client.get("/api/artists/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # --- ARTWORK TESTS ---
    def test_admin_can_create_artwork(self):
        self.client.force_authenticate(user=self.admin_user)
        image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        response = self.client.post(
            "/api/artworks/",
            {
                "title": "New Artwork",
                "artist": self.artist.id,
                "date": "2024-01-01",
                "movement": "New Style",
                "image": image  # Include an image
            },
            format="multipart"  # Required for file uploads
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_anyone_can_get_artworks(self):
        self.client.force_authenticate(user=self.end_user)
        response = self.client.get("/api/artworks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # --- ESSAY TESTS ---

    def test_author_can_create_essay(self):
        self.client.force_authenticate(user=self.author_user)
        response = self.client.post(
            "/api/essays/",
            {"title": "New Essay", "content": "Essay Content", "author": self.author_user.id, "artwork": self.artwork.id}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_cannot_create_essay(self):
        self.client.force_authenticate(user=self.end_user)
        response = self.client.post(
            "/api/essays/",
            {"title": "New Essay", "content": "Essay Content", "author": self.end_user.id, "artwork": self.artwork.id}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anyone_can_get_essays(self):
        self.client.force_authenticate(user=self.end_user)
        response = self.client.get("/api/essays/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # --- COMMENT TESTS ---

    def test_anyone_can_comment(self):
        self.client.force_authenticate(user=self.end_user)
        response = self.client.post(
            "/api/comments/",
            {"content": "Nice Artwork!", "artwork": self.artwork.id, "user": self.end_user.id}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_anyone_can_get_comments(self):
        self.client.force_authenticate(user=self.end_user)
        response = self.client.get("/api/comments/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
