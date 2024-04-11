from rest_framework import serializers

from .models import User, UserGroup


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'created_at', 'updated_at']
        fields_read_only = ['id', 'created_at', 'updated_at']


class UserSerializer(BaseSerializer):
    '''
    Serializer for User model
    '''
    class Meta:
        model = User
        fields = '__all__'
        
    
class UserGroupSerializer(BaseSerializer):
    '''
    Serializer for User group model
    '''
    class Meta:
        model = UserGroup
        fields = BaseSerializer.Meta.fields + ['name']