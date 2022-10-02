from django.test import TestCase
from django.contrib.auth.models import User, Group
from visitors.models import (Reservation, Room, Floor)
from accounts.models import Visitor
from datetime import date, timedelta
from django.urls import reverse

from visitors.tests.common.mixins import TestDataMixin


class ReservationListViewTest(TestDataMixin, TestCase):

    @classmethod
    def setUpTestData(cls):

        user, rooms, check_in, check_out = super().setUpTestData()

        reservation = Reservation.objects.create(check_in= check_in, check_out=check_out, 
        visitor=user.visitor, active=True)
        reservation.rooms.add(rooms[0])

    def test_check_redirect(self):

        response = self.client.get(reverse('reservations'))
        self.assertEqual(response.status_code, 302)

    def test_get_reservation_list(self):
        
        self.client.login(username='test', password='1234!')

        response = self.client.get(reverse('reservations'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, date.today())
        self.assertContains(response, 'CHECKIN')

