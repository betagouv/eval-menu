from django.db.models.signals import post_save
from django.dispatch import receiver

from ecobalyse import import_data
from data.models.recette import RecetteIngredient


@receiver(post_save, sender=RecetteIngredient)
def ingredients_changed(sender, instance, **kwargs):
    print(instance.recette.name)
    import_data.update_score_for_recette(instance.recette)
