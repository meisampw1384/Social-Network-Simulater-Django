from rest_framework import serializers

from django.contrib.auth import get_user_model

from .models import Friendship


User = get_user_model()


class UserListSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('id','username','avatar')
        
    def get_avatar(self,instanse):
        if hasattr(instanse , 'profile') and instanse.profile.avatar:
            return instanse.profile.avatar.url
        return ''
        
