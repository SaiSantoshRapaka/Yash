from django.urls import include, path
from .views import profiles

urlpatterns = [
    path('profile/', profiles.as_view()),
    
]