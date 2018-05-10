from django.contrib.auth import get_user_model
from django.test import TestCase

from django.urls import reverse

from jmbo.models import Relation

from post.models import Post


class ViewsTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        super(ViewsTestCase, cls).setUpTestData()

        # Post
        obj, dc = Post.objects.get_or_create(
            title="Post",
            markdown="""aaaa
***
bbb""",
            state="published",
        )
        obj.save()
        obj.sites.set([1])
        obj.save()
        cls.post = obj

    def test_pagination(self):
        response = self.client.get(self.post.get_absolute_url())
        # django-pagination-fork 1.0.17 can"t handle the hashtag argument yet
        #self.failUnless("<a href="?page=2#jmbo-post"" in response.content)
        self.failUnless("<a href=\"?page=2\"" in response.content.decode("utf-8"))
