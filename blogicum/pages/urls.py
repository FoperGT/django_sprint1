from django.urls import path
from .views import about, rules

urlspatterns = [
    path('about/', about, name='about'),
    path('rules', rules, name='rules'),
]