from rest_framework import generics
from rest_framework import permissions

from accounts.models import Author
from .models import Post, Comment, StatusPost
from .permissions import IsAuthorPermission
from .serializers import PostSerializer, CommentSerializer, StatusPostSerializer


class PostCreateApiView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.author)


class PostRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorPermission | permissions.IsAdminUser]


class CommentCreateApiView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return super().get_queryset().filter(post_id=self.kwargs.get('post_id'))

    def perform_create(self, serializer):
        user1 = Author.objects.all().first()
        if self.request.user.is_anonymous:
            serializer.save(
                author=user1,
                post_id=self.kwargs.get('post_id')
            )
        else:
            serializer.save(
                author=self.request.user.author,
                post_id=self.kwargs.get('post_id')
            )


class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, permissions.IsAdminUser]


class StatusPost(generics.ListCreateAPIView):
    queryset = StatusPost.objects.all()
    serializer_class = StatusPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get_queryset(self):
        return super().get_queryset().filter(post_id=self.kwargs.get('post_id'))

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user.author,
            post_id=self.kwargs.get('post_id')
        )