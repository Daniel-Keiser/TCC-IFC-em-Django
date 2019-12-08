from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'main'

class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals