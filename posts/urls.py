from django.urls import path

from .views import PostView,PostDetailView

urlpatterns = [
    path('post/',PostView.as_view(), name = 'post'),
    path('post/list_post/',PostView.as_view()),
    path('post/<int:post_pk>/',PostDetailView.as_view())
]
