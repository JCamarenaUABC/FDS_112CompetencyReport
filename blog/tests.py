from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post

class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.post=Post.object.create(
            title='A good title',
            body='Nice',
            author=self.username
        )

    def test_string_representation(self):
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)

    def test_get_absolute_url(self):
        self.assertEqual(self.post.test_get_absolute_url(),'/post/1/')
        
    def test_post_content(self):
        self.assertEqual(f'{self.post.title}','A goog title')
        self.assertEqual(f'{self.post.author}','Yo mero')
        self.assertEqual(f'{self.post.body}','Nice body')
    



        

