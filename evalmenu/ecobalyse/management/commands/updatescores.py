from django.core.management.base import BaseCommand

from ecobalyse import import_data


class Command(BaseCommand):
    help = "Call Ecobalyse API"

    def handle(self, *args, **options):
        import_data.update_scores()
