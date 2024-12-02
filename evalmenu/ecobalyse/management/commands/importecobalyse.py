from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Import Ecobalyse ingredients"

    def add_arguments(self, parser):
        parser.add_argument("ingredients_file", type=str)

    def handle(self, *args, **options):
        ingredients_file = options["ingredients_file"]
        self.stdout.write(self.style.NOTICE(f"Importing file {ingredients_file}"))
