"""
This module contains test files.
"""

from django.test import TestCase
from django.urls import reverse

from .models import Blogs, User


class ModelTest(TestCase):
    """
    This class contains tests for models.
    """

    def test_user_str(self):
        """
        Test the string representation of the User model.
        """
        user = User.objects.create(username="keval")
        self.assertEqual(str(user), "keval")

    def test_blog_str(self):
        """
        Test the string representation of the Blog model.
        """
        user = User.objects.create(username="keval")
        blog = Blogs.objects.create(
            title="Blog testing", description="testing", author=user
        )
        self.assertEqual(str(blog), "Blog testing")

    def test_get_absolute_url(self):
        """
        Test the get_absolute_url method of the Blog model.
        """
        user = User.objects.create(username="testuser")
        blog = Blogs.objects.create(title="Test Blog", description="Test", author=user)
        self.assertEqual(blog.get_absolute_url(), f"/blog/{blog.id}/")


class ViewsTest(TestCase):
    """
    This class contains tests for views.
    """

    @classmethod
    def data_for_test(cls):
        """
        Prepare data for testing.
        """
        number_of_blogs = 13
        user = User.objects.create(username="testuser")
        for blog_num in range(number_of_blogs):
            Blogs.objects.create(
                title=f"Test Blog {blog_num}", description="Test", author=user
            )

    def test_url_at_specific_location(self):
        """
        Test if the URL is accessible at a specific location.
        """
        response = self.client.get("/blog/blogs/")
        self.assertEqual(response.status_code, 200)

    def test_name_url(self):
        """
        Test if the named URL is accessible.
        """
        response = self.client.get(reverse("blog"))
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        """
        Test if the correct template is used.
        """
        response = self.client.get(reverse("blogs_lists"))
        self.assertTemplateUsed(response, "blog_lists.html")

    def test_pagination_is_five(self):
        """
        Test if pagination is set to five.
        """
        response = self.client.get(reverse("blogs_lists"))
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"] is True)
        self.assertEqual(len(response.context["blogs"]), 5)
