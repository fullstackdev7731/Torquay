from time import time
from django.urls import path
from .views import Homepage

urlpatterns = [
    path('homepage/', Homepage.as_view(), name='staff_homepage'),
]




# Why use:
# - code quality
# - reliability

# - less time

# - debugging 

# - system integration

# Why not use:
# - hackaton
# - POC - prototype 