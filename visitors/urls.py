from django.urls import path
from .views import (visitor_homepage,
                    create_reservation,
                    RoomView,
                    ReservationList,
                    ReservationView)
urlpatterns = [
    path('homepage', visitor_homepage, name='visitor_homepage'),
    path('create_reservation', create_reservation, name='create_reservation'),
    path('reservations', ReservationList.as_view(), name='reservations'),
    path('reservation-detail/<int:pk>', ReservationView.as_view(), name='reservation_detail'),
    path('room-detail/<int:pk>', RoomView.as_view(), name='room_detail')   
]
