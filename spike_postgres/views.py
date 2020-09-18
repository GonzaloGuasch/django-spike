from .models import Disease
from rest_framework import viewsets, status
from .serializers import DiseaseSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User


class DiseaseView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer


class UserCreate(APIView):
    def get(self, *args):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)