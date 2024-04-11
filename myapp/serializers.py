from rest_framework import serializers
from .models import Employee

class BaseSerializer(serializers.ModelSerializer):
    '''
    Base serializer for all retest_app serializers
    '''
    class Meta:
        fields = ['id', 'created_at', 'updated_at']
        fields_read_only = ['id', 'created_at', 'updated_at']

class EmployeeSerializer(serializers.ModelSerializer):
    '''
    Employee serializer
    '''
    class Meta:
        model = Employee
        fields = BaseSerializer.Meta.fields + ['name', 'id_number', 'date_of_joining', \
                                                'salary', 'active']