from django.test import TestCase
from blog.forms import PostForm

class PostFormTest(TestCase):
    def test_valid_form(self):
        form = PostForm(data={'title': 'Form Test', 'content': 'Works!'})
        self.assertTrue(form.is_valid())