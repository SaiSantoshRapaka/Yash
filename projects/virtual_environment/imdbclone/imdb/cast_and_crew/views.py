from django.shortcuts import render
from rest_framework.views import APIView
from .models import *

# Create your views here.

class CreateOrUpdateMovie(APIView):
    def post(self, request, slug):
        try:
            req = request.data
            movie_name = req["movie_name"]
            hero = req["hero"]
            heroine = req["heroine"]
            director = req["director"]
            release_date = req["release_date"]
            genere = req["genere"]
            plot = req["plot"]
            movies.objects.create(movie_name = movie_name, hero = hero, heroine = heroine, director = director, release_date = release_date, genere = genere, plot = plot)

        except:
            pass
    def get(self, slug):
        try:
            movies.objects.get(movie_name = slug)

        except:
            pass