from django.apps import AppConfig


class SleepingBedsConfig(AppConfig):
    name = 'sleeping_beds'
    
    def ready(self):
        from . import signals