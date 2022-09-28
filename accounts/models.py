from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField
from country_list import countries_for_language
# Create your models here.

class Visitor(models.Model):
    COUNTRIES = countries_for_language('en') 

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='visitor')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=10, choices=COUNTRIES)

    # class Meta:
    #     unique_together = ['first_name', 'last_name', 'email', 'phone_number']
    
    def __str__(self):
        return f"{self.first_name}, {self.email}"


def post_profile_group(sender, instance, created, *args, **kwargs):
    if created:
        if not instance.is_staff:
            Visitor.objects.create(user_id = instance.id)
            Group.objects.get(name='Visitors').user_set.add(instance)

post_save.connect(receiver=post_profile_group, sender=User)
