from django.apps import AppConfig


class EcobalyseConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ecobalyse"

    def ready(self):
        import ecobalyse.handlers  # noqa
