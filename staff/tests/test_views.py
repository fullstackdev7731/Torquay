from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class HomepageTest(TestCase):

    def test_status_code(self):
        response = self.client.get(reverse('staff_homepage'))
        self.assertEqual(response.status_code, 200)
    
    def test_template(self):
        response = self.client.get(reverse('staff_homepage'))
        self.assertTemplateUsed(response, "staff_homepage.html")