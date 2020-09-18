from .models import Disease
from rest_framework import viewsets
from .serializers import DiseaseSerializer
from rest_framework.permissions import IsAuthenticated


class DiseaseView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer
