from django.db.models.signals import post_save
from django.dispatch import receiver

from data.models.recette import RecetteIngredient
from api.utils import get_nutriscore
from ecobalyse import import_data


@receiver(post_save, sender=RecetteIngredient)
def ingredients_changed(sender, instance, **kwargs):
    print(instance.recette.name)
    import_data.update_score_for_recette(instance.recette)

    recettes_ingredients = RecetteIngredient.objects.filter(
        recette_id=instance.recette.id
    ).select_related("recette", "ingredient")
    ingredients = []

    for recette_ingredient in recettes_ingredients:
        print(f"{recette_ingredient.recette} - {recette_ingredient.ingredient}")
        name = (
            recette_ingredient.ingredient.name.replace(" FR ou UE ou Hors UE Bio", "")
            .replace(" UE Conv.", "")
            .replace(" FR Conv.", "")
            .replace("Colin", "Poisson colin")
        )
        ingredients.append(name + " " + str(int(recette_ingredient.poids)) + "g")

    score = get_nutriscore(", ".join(ingredients))

    print(f"Got nutriscore {score}")
    if score != "unknown":
        instance.recette.nutriscore = score.upper()
        instance.recette.save()
