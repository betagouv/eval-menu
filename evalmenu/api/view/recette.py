from django.contrib.auth.models import Group, User

from rest_framework.generics import (
    ListAPIView,
)
from data.models.recette import Recette
from api.serializers.recette import RecetteSerializer


class RecetteView(ListAPIView):
    """
    API endpoint that allows recette to be viewed.
    """
    queryset = Recette.objects.all()
    serializer_class = RecetteSerializer
