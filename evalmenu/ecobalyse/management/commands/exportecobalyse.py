from django.core.management.base import BaseCommand

from ecobalyse import export_data


class Command(BaseCommand):
    help = "Export databse ingredients"

    def add_arguments(self, parser):
        parser.add_argument("export_path", type=str)
        #TODO possibility to use no arg
        
    def handle(self, *args, **options):
        export_file = options["export_path"]
        export_data.export_recipes(export_file)
