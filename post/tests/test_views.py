import unittest

from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.test.client import Client, RequestFactory

from jmbo.models import Relation

from post.models import Post


class ViewsTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = Client()

        # Post
        obj, dc = Post.objects.get_or_create(
            title="Post",
            content="""aaaa <div style="page-break-after: always;"></div>bbb""",
            state="published",
        )
        obj.sites = [1]
        obj.save()
        cls.post = obj

    def test_pagination(self):
        response = self.client.get(self.post.get_absolute_url())
        # django-pagination-fork 1.0.17 can"t handle the hashtag argument yet
        #self.failUnless("<a href="?page=2#jmbo-post"" in response.content)
        self.failUnless("<a href=\"?page=2\"" in response.content)
