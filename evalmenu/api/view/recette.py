from django.contrib.auth.models import Group, User
from rest_framework import viewsets
from rest_framework.generics import (
    ListAPIView, 
)
from rest_framework import status
from rest_framework.response import Response
from data.models.recette import Recette
from api.serializers.recette import RecetteSerializer
from rest_framework.permissions import AllowAny

class RecetteViewSet(viewsets.ViewSet):
    """
    API endpoint that allows recette to be viewed.
    """
    queryset = Recette.objects.all()
    serializer_class = RecetteSerializer
    permission_classes = [AllowAny]  # Allow all requests  

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()  # Fetch all objects
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

