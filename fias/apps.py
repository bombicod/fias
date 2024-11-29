from django.apps import AppConfig


class FiasAppConfig(AppConfig):
    name = 'fias'
    verbose_name = 'ФИАС'
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        import fias.signals
