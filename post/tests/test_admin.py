import unittest

from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.test.client import Client, RequestFactory

from jmbo.models import Relation

from post.models import Post


class AdminTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = Client()

        # Editor
        cls.editor = get_user_model().objects.create(
            username="editor",
            email="editor@test.com",
            is_superuser=True,
            is_staff=True
        )
        cls.editor.set_password("password")
        cls.editor.save()
        cls.client.login(username='editor', password='password')

        # Post
        obj, dc = Post.objects.get_or_create(
            title='Post',
            content='aaaa <div style="page-break-after: always;"></div>bbb',
            owner=cls.editor, state='published',
        )
        obj.sites = [1]
        obj.save()
        cls.post = obj

        # Create a relation. Easier to test here than in Jmbo itself.
        obj = Relation.objects.create(
            source_content_type=cls.post.content_type,
            source_object_id=0,
            target_content_type=cls.post.content_type,
            target_object_id=0,
            name="post_posts"
        )

    def setUp(self):
        self.client.logout()

    def test_admin_add(self):
        self.client.login(username="editor", password="password")
        response = self.client.get("/admin/post/post/add/")
        self.assertEquals(response.status_code, 200)

    def test_admin_change(self):
        self.client.login(username="editor", password="password")
        response = self.client.get("/admin/post/post/%s/change/" % self.post.pk)
        self.assertEquals(response.status_code, 200)

    def test_admin_relation(self):
        self.client.login(username="editor", password="password")
        response = self.client.get("/admin/post/post/add/")
        self.failUnless("Post posts" in response.content)
