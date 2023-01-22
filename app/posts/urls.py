from django.urls import path

from . import views as post_view


urlpatterns = [
    path('api/posts/', post_view.PostCreateApiView.as_view()),
    path('api/posts/<int:pk>/', post_view.PostRetrieveUpdateDestroyApiView.as_view()),

    path('api/posts/<int:post_id>/comments/', post_view.CommentCreateApiView.as_view()),
    path('api/posts/<int:post_id>/comments/<int:pk>/', post_view.CommentRetrieveUpdateDestroyAPIView.as_view()),

    path('api/posts/rating/<int:post_id>/', post_view.StatusPost.as_view()),
]