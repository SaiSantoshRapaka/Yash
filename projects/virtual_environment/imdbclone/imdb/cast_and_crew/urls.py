from django.urls import path
from .views import *

urlpatterns = [
    path('movie/<slug:slug>',CreateOrUpdateMovie.as_view()),
]