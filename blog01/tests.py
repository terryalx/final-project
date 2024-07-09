from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from pathlib import Path
from blog01.models import BlogPost
from django.core.files.uploadedfile import SimpleUploadedFile

class BlogPostModelTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.image = self.create_test_image()

    def create_test_image(self):
        image = Image.new('RGB', size=(800, 600))
        image_io = BytesIO()
        image.save(image_io, format='JPEG')
        image_io.seek(0)
        return image_io

    def test_create_blog_post(self):
        image_file = SimpleUploadedFile("test_image.jpg", self.image.read())

        post = BlogPost.objects.create(
            title='Test Post',
            author=self.user,
            image=image_file,
            tag='test',
            date=timezone.now()
        )
        self.assertEqual(str(post), 'Test Post - test')
