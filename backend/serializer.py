from rest_framework import serializers
from .models import RD
from .models import DB

class RDSerializer(serializers.ModelSerializer):
    class Meta:
        model = RD
        fields = ['id', 'member', 'position', 'remarks', 'created_at']
        read_only_fields = ['id', 'created_at']

class DBSerializer(serializers.ModelSerializer):
    class Meta:
        model = DB
        fields = ['id', 'member', 'position', 'remarks', 'created_at']
        read_only_fields = ['id', 'created_at']
