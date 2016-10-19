from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers
from rest_framework_extras import discover

from post import api as post_api


admin.autodiscover()

router = routers.SimpleRouter()
post_api.register(router)
discover(router)

urlpatterns = [
    url(r"^admin/", include(admin.site.urls)),
    url(r'^api/(?P<version>(v1))/', include(router.urls)),
    url(r"^jmbo/", include("jmbo.urls", namespace="jmbo")),
    url(r"^ckeditor/", include("ckeditor.urls")),
    url(r"^post/", include("post.urls", namespace="jmbo")),
    url(r"^comments/", include("django_comments.urls")),
]
