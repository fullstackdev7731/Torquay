from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User, Group
from visitors.models import (Reservation, Room, Floor)
from accounts.models import Visitor
from datetime import date, timedelta
from visitors import views
from django.urls import reverse

from visitors.tests.common.mixins import TestDataMixin


class ReservationListViewTest(TestCase):

    fixtures = ['groups.json', 'users.json', 'visitors.json', 'floor.json', 'rooms.json', 'reservations.json']

    def test_check_redirect(self):

        response = self.client.get(reverse('reservations'))
        self.assertEqual(response.status_code, 302)

    def test_get_reservation_list(self):
        
        self.client.login(username='pol', password='postgres')
        reservation = Reservation.objects.filter(visitor__first_name = 'Pol').first()
        response = self.client.get(reverse('reservations'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, reservation.check_in)
        self.assertContains(response, 'CHECKIN')


class ReservationViewTest(TestCase):

    fixtures = ['groups.json', 'users.json', 'visitors.json', 'floor.json', 'rooms.json', 'reservations.json']

    def setUp(self):
        self.factory = RequestFactory()
        self.visitor = User.objects.get(username='pol').visitor

    def test_reservation(self):
        kwargs = {'pk': self.visitor.reservations.last().id}
        request = self.factory.get(reverse('reservation_detail', kwargs=kwargs))
        response = views.ReservationView.as_view()(request, **kwargs)

        self.assertEqual(response.status_code, 200)
        room_numbers = list(self.visitor.reservations.last().rooms.all().values_list(
            'number', flat=True
        ))

        self.assertContains(response, 'HELLO')
        for room in room_numbers:
            self.assertContains(response, room)












    # @classmethod
    # def setUpTestData(cls):

    #     user, rooms, check_in, check_out = super().setUpTestData()

    #     reservation = Reservation.objects.create(check_in= check_in, check_out=check_out, 
    #     visitor=user.visitor, active=True)
    #     reservation.rooms.add(rooms[0])