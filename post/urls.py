from django.conf.urls import include, url

from jmbo.views import ObjectDetail

app_name = "post"
urlpatterns = [
    url(
        r"^(?P<category_slug>[\w-]+)/(?P<slug>[\w-]+)/$",
        ObjectDetail.as_view(),
        name="post-categorized-detail"
    ),
    url(
        r"^(?P<slug>[\w-]+)/$",
        ObjectDetail.as_view(),
        name="post-detail"
    ),
]
