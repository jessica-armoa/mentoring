from django.db import migrations, models

def create_google_meet_rooms(apps, schema_editor):
    GoogleMeetRoom = apps.get_model('app', 'GoogleMeetRoom')  # Replace 'your_app_name' with the actual app name
    rooms_data = [
        {"room_name": "sala1", "room_link": "https://meet.google.com/xke-tibc-qdu", "is_occupied": False},
        {"room_name": "sala2", "room_link": "https://meet.google.com/khi-razy-rgq", "is_occupied": False},
    ]
    rooms = [GoogleMeetRoom(**data) for data in rooms_data]
    GoogleMeetRoom.objects.bulk_create(rooms)

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_areas'),
    ]

    operations = [
        migrations.RunPython(create_google_meet_rooms)
    ]
