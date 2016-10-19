import markdown
from bs4 import BeautifulSoup

from django.db import models
from django.core.urlresolvers import reverse

from ckeditor.fields import RichTextField

from jmbo.models import ModelBase


class Post(ModelBase):
    autosave_fields = ("markdown",)

    markdown = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    @property
    def content(self):
        return markdown.markdown(self.markdown)

    @property
    def content_pages(self):
        if not self.content:
            return ""
        marker = "--m-a-r-k-er--"
        soup = BeautifulSoup(self.content)
        elems = soup.find_all("hr")
        for elem in elems:
            elem.replace_with(marker)
        return soup.renderContents().split(marker)
