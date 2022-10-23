import os
from tkinter import N
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Torquay.settings')
django.setup()

from visitors.models import Room, Floor
import random 
def create_rooms(n):

    for f in range(1,5):
        print(f'Floor {f}')
        for new in range(n):
            print(f'Room {n}')
            created = False
            while not created:
                beds = random.randint(2,6)
                floor = Floor.objects.get(number=f)
                new_room = Room(floor=floor, beds=beds)
                new_room.save()
                created = True
                print(f"created room {new_room.number}")



if __name__ == '__main__':
    print("Populating database")
    create_rooms(50)