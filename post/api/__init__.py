from rest_framework.serializers import ReadOnlyField, Serializer

from jmbo import api as jmbo_api

from post.models import Post


class PropertiesMixin(Serializer):
    content = ReadOnlyField()
    content_pages = ReadOnlyField()

    class Meta:
        fields = ("content", "content_pages")


class PostSerializer(
    PropertiesMixin, jmbo_api.ModelBaseSerializer
    ):

    class Meta(jmbo_api.ModelBaseSerializer.Meta):
        pass


class PostObjectsViewSet(jmbo_api.ModelBaseObjectsViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostPermittedViewSet(jmbo_api.ModelBasePermittedViewSet):
    queryset = Post.permitted.all()
    serializer_class = PostSerializer


def register(router):
    router.register(
        r"post-post",
        PostObjectsViewSet,
    )
    router.register(
        r"post-post-permitted",
        PostPermittedViewSet,
    )
