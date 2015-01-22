from django.test import TestCase as BaseTestCase
from django.test.client import Client as BaseClient, RequestFactory
from django.contrib.auth.models import User

from post.models import Post


class TestCase(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        cls.request = RequestFactory()
        cls.client = BaseClient()

        # Editor
        cls.editor, dc = User.objects.get_or_create(
            username='editor',
            email='editor@test.com'
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

    def test_pagination(self):
        response = self.client.get(self.post.get_absolute_url())
        self.failUnless('<a href="?page=2#jmbo-post"' in response.content)

    def test_admin_add(self):
        response = self.client.get("/admin/post/post/add/")
        self.assertEquals(response.status_code, 200)
