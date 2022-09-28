from django.urls import path
from .views import (register, 
                    user_login, 
                    user_logout,
                    update_profile,
                    profile)

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('update-profile/', update_profile, name='update-profile'),
    path('profile/', profile, name='profile'),
]
