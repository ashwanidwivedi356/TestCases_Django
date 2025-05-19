from django.test import TestCase
from blog.models import Post

class PostModelTest(TestCase):
    def test_str(self):
        post = Post.objects.create(title="Test", content="Test content")
        self.assertEqual(str(post), "Test")
