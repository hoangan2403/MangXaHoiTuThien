
from rest_framework import viewsets, generics, status
from rest_framework.response import Response

from socialnetworks.models import Post, Auction
from socialnetworks import serializers, paginators
from rest_framework.decorators import action


class PostViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Post.objects.filter(active=True).all().order_by('-created_date')
    serializer_class = serializers.PostSerializer
    # pagination_class = paginators.PostPaginator

    def get_queryset(self):
        queries = self.queryset

        q = self.request.query_params.get("q")
        if q:
            queries = queries.filter(post_hashtag__name__exact=q)

        return queries

    @action(methods=['get'], detail=True)
    def comments(self, request, pk):
        comments = self.get_object().comments_set.all().order_by('-created_date')

        # import pdb
        # pdb.set_trace()

        return Response(serializers.CommentSerializer(comments, many=True, context={'request': request}).data,
                        status=status.HTTP_200_OK)

class AuctionViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Auction.objects.all();
    serializer_class = serializers.AuctionSerializer
    # pagination_class = paginators.PostPaginator