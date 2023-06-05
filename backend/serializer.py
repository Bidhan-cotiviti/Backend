from rest_framework import serializers
from .models import RD
from .models import DB

class RDSerializer(serializers.ModelSerializer):
    class Meta:
        model = RD
        fields = ['emp_id', 'member', 'position', 'remarks', 'created_at']
        read_only_fields = ['created_at']

class DBSerializer(serializers.ModelSerializer):
    class Meta:
        model = DB
        fields = ['emp_id', 'member', 'position', 'remarks', 'created_at']
        read_only_fields = ['created_at']
