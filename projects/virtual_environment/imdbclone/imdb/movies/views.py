from django.shortcuts import render, redirect 
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import *

# Create your views here.

class MoviesView(APIView):
        
    def post(self, request):
        try:
            req = request.data
            movie_name = req["movie_name"]
            hero = req["hero"]
            heroine = req["heroine"]
            director = req["director"]
            release_date = req["release_date"]
            genere = req["genere"]
            genere = generes.objects.get(genere = genere)
            plot = req["plot"]    
            movies.objects.create(movie_name = movie_name, hero = hero, heroine = heroine, director = director,release_date = release_date , genere = genere, plot = plot)
            final_response = {"Status": "Movie_Created"}
            return JsonResponse(final_response)
    
        except:
            final_response = {"Status": "Something went wrong"}
            return JsonResponse(final_response)
        

    def get(self,request):
        list1 = []
        req = movies.objects.all()
        #print(req)
        for ins in range(len(req)):
            movie_name = req[ins].movie_name
            #print(movie_name)
            hero = req[ins].hero
            heroine = req[ins].heroine
            director = req[ins].director
            release_date = str(req[ins].release_date)
            genere = str(req[ins].genere)
            plot = req[ins].plot
            updated = str(req[ins].updated)
            movie_dict = {"movie_name" : movie_name, "hero" : hero, "heroine" : heroine, "director" : director, "release_date" : release_date, "genere" : genere, "plot" : plot, "updated":updated}
            list1.append(movie_dict)
        final_response = {"data":list1}
        print(final_response)
        return JsonResponse(final_response)
    

    
    
class MovieView(APIView):
    def get(self,request,pk):
        print(pk)
        list1 = []
        req = movies.objects.get(movie_name = pk)
        print(req)
        for ins in range(1):
            movie_name = req.movie_name
            #/print(movie_name)
            hero = req.hero
            heroine = req.heroine
            director = req.director
            release_date = str(req.release_date)
            genere = str(req.genere)
            plot = req.plot
            updated = str(req.updated)
            movie_dict = {"movie_name" : movie_name, "hero" : hero, "heroine" : heroine, "director" : director, "release_date" : release_date, "genere" : genere, "plot" : plot, "updated":updated}
            list1.append(movie_dict)
        final_response = {"data":list1}
        return JsonResponse(final_response)
    
    def put(self,request,pk):
        req = request.data
        movie_name = req["movie_name"]
        hero = req["hero"]
        heroine = req["heroine"]
        director = req["director"]
        release_date = req["release_date"]
        genere = req["genere"]
        genere = generes.objects.get(genere = genere)
        plot = req["plot"]    
        movie_to_be_updated = movies.objects.get(movie_name = pk)
        movie_to_be_updated.movie_name = movie_name
        movie_to_be_updated.hero = hero
        movie_to_be_updated.heroine = heroine
        movie_to_be_updated.director = director
        movie_to_be_updated.release_date = release_date
        movie_to_be_updated.genere = genere
        movie_to_be_updated.plot = plot
        movie_to_be_updated.save()
        
        final_response = {"Status": "Movie_Updated"}
        return JsonResponse(final_response)
    
    def delete(self,request,pk):
        req = movies.objects.get(movie_name = pk)
        req.delete()
        final_response = {"Status": "Movie_Deleted"}
        return JsonResponse(final_response)
