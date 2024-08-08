from rest_framework import serializers
from .models import ExpTable

class S_ExpTable(serializers.ModelSerializer):
    class Meta:
        model = ExpTable
        fields = '__all__'