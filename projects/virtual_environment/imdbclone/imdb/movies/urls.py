from django.urls import path
from .views import *

urlpatterns = [
    path('movies/',MoviesView.as_view()),
    path('movie/<str:pk>/',MovieView.as_view()),
]