from django.apps import AppConfig


class PostsConfig(AppConfig):
    name = 'posts'
      
    def redy(self):
        import posts.signals