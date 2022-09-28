import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Torquay.settings')
django.setup()

from visitors.models import Room, Floor
import random 
def create_rooms(n):
    for f in range(1,5):
        for new in range(n):
            created = False
            while not created:
                try:
                    beds = random.randint(10,20)
                    floor = Floor.objects.get(number=f)
                    new_room = Room(floor=floor, beds=beds)
                    new_room.save()
                    created = True
                except:
                    continue


if __name__ == '__main__':
    print("Populating database")
    create_rooms(1)