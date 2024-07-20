from django.urls import path

from .views import UserListView,RequestView


urlpatterns = [
    path('users-list/', UserListView.as_view()),
    path('request/',RequestView.as_view()),
    # path('request-list/'),
    # path('accept/'),
    # path('friends/')
]
