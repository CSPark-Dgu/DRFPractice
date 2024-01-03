from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# def post_list(request):   #원래는 이런 식으로 구현해야 함
#     pass
#
# def post_detial(request, pk):
#     pass
