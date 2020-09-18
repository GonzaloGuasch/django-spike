from .models import Disease
from rest_framework import serializers


class DiseaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Disease
        fields = '__all__'