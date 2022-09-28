from django.urls import path
from .views import Homepage, reservation_search

urlpatterns = [
    path('homepage/', Homepage.as_view(), name='staff_homepage'),
    path('search/', reservation_search, name='reservation_search'),
]