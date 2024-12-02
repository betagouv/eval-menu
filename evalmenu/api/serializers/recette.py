from data.models.recette import Recette
from rest_framework import serializers


class RecetteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recette
        fields = ['id', 'name']
