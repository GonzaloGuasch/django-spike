from .models import Disease
from rest_framework import viewsets
from .serializers import DiseaseSerializer


class DiseaseView(viewsets.ModelViewSet):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer
