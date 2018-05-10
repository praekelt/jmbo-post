import markdown
from bs4 import BeautifulSoup

from django.db import models
from django.urls import reverse

from simplemde.fields import SimpleMDEField

from jmbo.models import ModelBase


class Post(ModelBase):
    autosave_fields = ("markdown",)

    markdown = SimpleMDEField(null=True, blank=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    @property
    def content(self):
        if not self.markdown:
            return ""
        return markdown.markdown(self.markdown)

    @property
    def content_pages(self):
        marker = "--m-a-r-k-er--"
        soup = BeautifulSoup(self.content, "html.parser")
        elems = soup.find_all("hr")
        for elem in elems:
            elem.replace_with(marker)
        return soup.encode_contents().decode("utf-8").split(marker)
