from data.models.recette import Recette
from rest_framework import serializers


class RecetteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recette
        fields = ['id', 'name']
