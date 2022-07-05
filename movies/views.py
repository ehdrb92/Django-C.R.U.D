import json
from turtle import title

from django.http import JsonResponse
from django.views import View

from movies.models import Actor, Actor_movie, Movie

class ActorView(View):
    def post(self, request):
        data = json.loads(request.body)
        Actor.objects.create(
            first_name = data['first_name'],
            last_name = data['last_name'],
            date_of_birth = data['date_of_birth']
        )

        return JsonResponse({'message':'created'}, status=201)

    def get(self, request):
        actors = Actor.objects.all()
        result = []

        for actor in actors:
            result.append(
                {
                    'first_name' : actor.first_name,
                    'last_name' : actor.last_name,
                    'data_of_birth' : actor.date_of_birth
                }
            )

        return JsonResponse({'result':result}, status=200)

class MovieView(View):
    def post(self, request):
        data = json.loads(request.body)
        Movie.objects.create(
            title = data['title'],
            release_date = data['release_date'],
            running_time = data['running_time']
        )

        return JsonResponse({'message':'created'}, status=201)

    def get(self, request):
        movies = Movie.objects.all()
        result = []

        for movie in movies:
            result.append(
                {
                    'title' : movie.title,
                    'release_date' : movie.release_date,
                    'running_time' : movie.running_time 
                }
            )

        return JsonResponse({'result':result}, status=200)

class Actor_movieView(View):
    def post(self, request):
        data = json.loads(request.body)
        ref_actor = Actor.objects.get(first_name = data['actor'])
        ref_movie = Movie.objects.get(title = data['title'])

        Actor_movie.objects.create(
            actor = ref_actor,
            movie = ref_movie
        )

        return JsonResponse({'message':'created'}, status=201)

    def get(self, request):
        actor_movies = Actor_movie.objects.all()
        result = []

        for actor_movie in actor_movies:
            result.append(
                {
                    'actor' : actor_movie.actor,
                    'movie' : actor_movie.movie
                }
            )

        return JsonResponse({'result':result}, status=200)