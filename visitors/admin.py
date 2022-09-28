from django.contrib import admin
from .models import Floor, Room, Reservation, Comment
# Register your models here.

admin.site.register(Floor)
admin.site.register(Room)
admin.site.register(Reservation)
admin.site.register(Comment)