from .models import Model
from rest_framework import serializers

class ModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Model
        fields='__all__'