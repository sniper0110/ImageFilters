from django.apps import AppConfig


class ImagefiltersConfig(AppConfig):
    name = 'imagefilters'

    def ready(self):
        import imagefilters.signals