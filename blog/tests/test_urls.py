from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import post_list

class UrlTest(SimpleTestCase):
    def test_list_url(self):
        url = reverse('post_list')
        self.assertEqual(resolve(url).func, post_list)
