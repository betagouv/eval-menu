from django.core.management.base import BaseCommand

from ecobalyse import import_data


class Command(BaseCommand):
    help = "Import Ecobalyse ingredients"

    def add_arguments(self, parser):
        parser.add_argument("ingredients_file", type=str)

    def handle(self, *args, **options):
        ingredients_file = options["ingredients_file"]

        import_data.import_ingredients(ingredients_file)
