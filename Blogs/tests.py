from django.test import TestCase
from .models import User, Blogs, Comments
from django.urls import reverse

class Model_Test(TestCase):

    def test_user_str(self):
        user = User.objects.create(username='keval')
        self.assertEqual(str(user), 'keval')

    def test_blog_str(self):
        blog = Blogs.objects.create(title='Blog testing', description='testing', author=User.objects.create(username='keval'))
        self.assertEqual(str(blog), 'Blog testing')

    def test_get_absolute_url(self):
        blog = Blogs.objects.create(title='Test Blog', description='Test', author=User.objects.create(username='testuser'))
        self.assertEqual(blog.get_absolute_url(), f'/blog/{blog.id}/')

class Views_Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_blogs = 13
        user = User.objects.create(username='testuser')
        for blog_num in range(number_of_blogs):
            Blogs.objects.create(title=f'Test Blog {blog_num}', description='Test', author=user)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/blog/blogs/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('blogs_lists'))
        self.assertTemplateUsed(response, 'blog_lists.html')

    def test_pagination_is_five(self):
        response = self.client.get(reverse('blogs_lists'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertEqual(len(response.context['blogs']), 5)

    def test_lists_all_blogs(self):
        response = self.client.get(reverse('blogs') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['blogs']), 5)