from django.contrib.auth import get_user_model

from rest_framework.validators import UniqueValidator
from rest_framework import serializers


User = get_user_model()
class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(requeired = True, validators=[UniqueValidator(queryset= User.objects.all())])
    password1 = serializers.CharField(required = True)
    password2 = serializers.CharField(required = True)
    
    class Meta:
        model = User
        fields = ('email','username','password1','password2','first_name','last_name')
        extra_kwargs = {'first_name':{'required' : False},'last_name':{'required' : True}}
        
    def validate(self,attrs):
        if attrs['password1']!=attrs['password2']:
            raise serializers.ValidationError({"password": 'passwords did not match'})
        return attrs
    def create(self,validate_data):
        user=User.objects.create(username=validate_data['username'],
                                 email=validate_data['email'],
                                 first_name=validate_data.get('first_name',''),
                                 last_name=validate_data.get('last_name',''))
        user.set_password(validate_data['password1'])
        user.save()