from data.models.recette import Recette
from rest_framework import serializers


class RecetteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recette
        fields = ['name', 'nutriscore', 'cs', 'cs_compare', 'type_plat', 'is_bio']
