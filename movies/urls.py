from django.urls import path

from movies.views import MovieView, ActorView, Actor_movieView

urlpatterns = [
    path('/actor', ActorView.as_view()),
    path('/movie', MovieView.as_view()),
    path('/actor_movie', Actor_movieView.as_view())
]