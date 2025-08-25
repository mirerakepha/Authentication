from django.apps import AppConfig


class AuthenticationappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authenticationapp'

    def ready(self):
        import authenticationapp.signals
