from django.urls import path

from .views import PostView,PostDetailView,CommentView,LikeView

urlpatterns = [
    path('post/',PostView.as_view(), name = 'post'),
    path('posts-list/',PostView.as_view(),name= 'post_list'),
    path('post/<int:post_pk>/',PostDetailView.as_view(),'post detail'),
    path('post/<int:post_pk>/comments/',CommentView.as_view(),name = "comment"),
    path('post/<int:post_pk>/likes/',LikeView.as_view(),name = 'like')
]
