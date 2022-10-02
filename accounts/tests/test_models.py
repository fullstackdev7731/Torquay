from django.test import TestCase
from django.contrib.auth.models import User, Group
from accounts.models import Visitor
 
class VisitorTest(TestCase):

    fixtures = [
        'groups.json',
        'users.json',
        'visitors.json'
    ]
    
    def setUp(self):
        """self.Attributes"""
        self.user = User.objects.get(username='pol')

    def test_create_visitor(self):
        visitor = Visitor.objects.get(user_id = self.user.id)
        
        self.assertTrue(isinstance(visitor, Visitor))
        self.assertEqual(visitor.user_id, self.user.id)
        
