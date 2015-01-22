from django.test import TestCase as BaseTestCase
from django.test.client import Client as BaseClient, RequestFactory
from django.contrib.auth.models import User

from jmbo.models import Relation

from post.models import Post


class TestCase(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        cls.request = RequestFactory()
        cls.client = BaseClient()

        # Editor
        cls.editor, dc = User.objects.get_or_create(
            username='editor',
            email='editor@test.com',
            is_superuser=True,
            is_staff=True,
        )
        cls.editor.set_password("password")
        cls.editor.save()

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

    def test_pagination(self):
        response = self.client.get(self.post.get_absolute_url())
        self.failUnless('<a href="?page=2#jmbo-post"' in response.content)

    def test_admin_add(self):
        self.client.login(username="editor", password="password")
        response = self.client.get("/admin/post/post/add/")
        self.assertEquals(response.status_code, 200)

    def test_admin_change(self):
        self.client.login(username="editor", password="password")
        response = self.client.get("/admin/post/post/1/")
        self.assertEquals(response.status_code, 200)

    def test_admin_relation(self):
        self.client.login(username="editor", password="password")
        response = self.client.get("/admin/post/post/add/")
        self.failUnless("Post posts" in response.content)
