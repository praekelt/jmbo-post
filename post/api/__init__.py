from jmbo import api as jmbo_api

from post.models import Post


class PostObjectsViewSet(jmbo_api.ModelBaseObjectsViewSet):
    queryset = Post.objects.all()


class PostPermittedViewSet(jmbo_api.ModelBasePermittedViewSet):
    queryset = Post.permitted.all()


def register(router):
    router.register(
        r"post-post",
        PostObjectsViewSet,
    )
    router.register(
        r"post-post-permitted",
        PostPermittedViewSet,
    )
