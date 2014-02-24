from bs4 import BeautifulSoup

from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField

from jmbo.models import ModelBase


class Post(ModelBase):
    autosave_fields = ('content',)

    content = RichTextField(
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    @property
    def content_pages(self):
        marker = '--m-a-r-k-er--'
        soup = BeautifulSoup(self.content)
        elems = soup.find_all('div', attrs={'style': 'page-break-after: always;'})
        for elem in elems:
            elem.replace_with(marker)
        return soup.renderContents().split(marker)
