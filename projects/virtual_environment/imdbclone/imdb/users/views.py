from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import *

# Create your views here.
class profiles(APIView):
    def post(self, request):
        req = request.data

        final_response = {'Status': "Success"}
        return JsonResponse(final_response)
    
    def get(self, request):
        req = request.data
        name = req['name']
        try:

            username = userdata.objects.get(name = name)
            final_response = {"Username":username.name}
        except:
            final_response = {"Status": "Something Went Wrong"}
        #print(final_response)
        return JsonResponse(final_response)
