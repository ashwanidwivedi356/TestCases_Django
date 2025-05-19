from django.test import TestCase
from django.urls import reverse
from blog.models import Post

class PostViewTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title="Hello", content="World")

    def test_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello")

    def test_detail_view(self):
        response = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "World")
