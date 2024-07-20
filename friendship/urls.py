from django.urls import path

from .views import UserListView,RequestView,RequestList,AcceptView,FriendListView


urlpatterns = [
    path('users-list/', UserListView.as_view()),
    path('request/',RequestView.as_view()),
    path('request-list/',RequestList.as_view()),
    path('accept/',AcceptView.as_view()),
    path('friends/',FriendListView.as_view())
]
