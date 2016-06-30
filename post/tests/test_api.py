import os
import unittest
import json

from django.contrib.auth import get_user_model

from rest_framework.test import APIClient

from post.models import Post


class APITestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = APIClient()

        # Editor
        cls.editor = get_user_model().objects.create(
            username="editor-api",
            email="editor-api@test.com",
            is_superuser=True,
            is_staff=True
        )
        cls.editor.set_password("password")
        cls.editor.save()

        # Prep
        cls.client.logout()

        # Post
        obj, dc = Post.objects.get_or_create(
            title="Post",
            markdown="""aaaa
***
bbb""",
            state="published",
        )
        obj.sites = [1]
        obj.save()
        cls.post = obj

    def setUp(self):
        self.client.logout()

    def test_post_detail(self):
        response = self.client.get(
            "/api/v1/post-post-permitted/%s/" % self.post.pk
        )
        as_json = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.failUnless("content" in as_json)
        self.failUnless("content_pages" in as_json)
