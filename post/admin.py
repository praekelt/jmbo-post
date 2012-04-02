from django.contrib import admin

from jmbo.admin import ModelBaseAdmin
from post.models import Post

admin.site.register(Post, ModelBaseAdmin)
