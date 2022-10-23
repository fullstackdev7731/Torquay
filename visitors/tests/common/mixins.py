from django.test import TestCase
from django.contrib.auth.models import User, Group
from visitors.models import (Reservation, Room, Floor)
from accounts.models import Visitor
from datetime import date, timedelta
from django.urls import reverse

class TestDataMixin(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        f_object = Floor.objects.create(number=2)

        room_200 = Room.objects.create(number=200, beds = 2, floor = f_object)
        room_201 = Room.objects.create(number=201, beds = 4, floor = f_object)
        room_202 = Room.objects.create(number=202, beds = 6, floor = f_object)

        rooms = (room_200, room_201, room_202)

        Group.objects.create(name='Visitors')
        user = User.objects.create_user(username='test', password='1234!', is_staff=False)

        check_in = date.today()
        check_out = check_in + timedelta(days=10)

        return user, rooms, check_in, check_out