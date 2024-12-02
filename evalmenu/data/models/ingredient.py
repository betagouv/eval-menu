from django.db import models
from recette import Recette


class Ingredient(models.Model):
    id = models.IntegerField(primary_key=True)
    id_ecobalyse = models.IntegerField()
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)



class RecetteIngredient(models.Model):
    receipt = models.ForeignKey(Recette, on_delete=models.CASCADE, related_name="recette_ingredients")
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="recette_ingredients")
    poids = models.DecimalField(max_digits=10, decimal_places=2, help_text="Poids (en gramme)")

    class Meta:
        unique_together = ('recette', 'ingredient')

    def __str__(self):
        return f"{self.ingredient.name} in {self.recette.name} ({self.poids}g)"

