from django.db import models
from data.models.ingredient import Ingredient


class Recette(models.Model):
    class Nutriscore(models.TextChoices):
        A = "A"
        B = "B"
        C = "C"
        D = "D"
        E = "E"

    class TypePlat(models.TextChoices):
        main = "main"
        starter = "starter"
        desert = "desert"

    name = models.CharField(max_length=30)
    ingredients = models.ManyToManyField(Ingredient, through="RecetteIngredient")
    nutriscore = models.CharField(
        choices=Nutriscore, max_length=1, null=True, default=None, blank=True
    )
    cs = models.IntegerField(
        help_text="Score environnemental", null=True, default=None, blank=True
    )

    cs_compare = models.IntegerField(
        help_text="Score environnemental comparé", null=True, default=None, blank=True
    )

    type_plat = models.CharField(choices=TypePlat, max_length=30, null=True)
    is_bio = models.BooleanField()

    def __str__(self):
        return self.name


class RecetteIngredient(models.Model):
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    poids = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="Poids (en gramme)"
    )

    def __str__(self):
        return f"{self.recette} - {self.ingredient} - {self.poids}"
