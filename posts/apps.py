from django.apps import AppConfig
from posts import resetupvotes


class PostsConfig(AppConfig):
    name = "posts"

    def ready(self):
        resetupvotes.start()
