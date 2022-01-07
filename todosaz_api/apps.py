from django.apps import AppConfig

class TodosazApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todosaz_api'

    def ready(self):
        import todosaz_api.signals