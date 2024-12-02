from django.db import models
from data.models.ingredient import Ingredient

class Recette(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    ingredients = models.ManyToManyField(Ingredient, through="RecetteIngredient")

    def __str__(self):
        return self.name


class RecetteIngredient(models.Model):
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    poids = models.DecimalField(max_digits=10, decimal_places=2, help_text="Poids (en gramme)")

    def __str__(self):
        return f"{self.recette} - {self.ingredient}"
