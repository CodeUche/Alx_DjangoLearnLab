from django.apps import AppConfig



class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'
    
    def ready(self):
        # Import signals to ensure they are registered
        import relationship_app.signals

class AccountConfig(AppConfig):
    name = 'relationship_app.account'
    verbose_name = "Account Management"

    def ready(self):
        # Import signals to ensure they are registered
        import relationship_app.signals

