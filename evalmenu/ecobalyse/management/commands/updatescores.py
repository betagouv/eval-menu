from django.core.management.base import BaseCommand
from data.models.recette import Recette

from ecobalyse import import_data


class Command(BaseCommand):
    help = "Call Ecobalyse API"

    def handle(self, *args, **options):
        recettes = Recette.objects.all()
        import_data.update_scores(recettes)
