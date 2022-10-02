from django.test import TestCase
from django.contrib.auth.models import User
from visitors.forms import ReservationForm

from datetime import date, timedelta
from django.urls import reverse

from visitors.tests.common.mixins import TestDataMixin

class ReservationFormTest(TestDataMixin, TestCase):
    
    def setUp(self):
        self.user = User.objects.get(username='test')
    
    def test_reservation_date(self):

        invalid_date = {
            'check_in': date.today() - timedelta(days=5),
            'check_out': date.today(),
            'room_size': 5 
        }

        form = ReservationForm(data=invalid_date)
        form.is_valid()
        self.assertTrue(form.errors)
    
    def test_reservation_correct(self):

        valid_data = {
            'check_in': date.today(),
            'check_out': date.today() + timedelta(days=5),
            'room_size': 3
        }

        form = ReservationForm(data=valid_data)
        form.is_valid()
        self.assertFalse(form.errors)
