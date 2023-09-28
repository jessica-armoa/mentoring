from django.core.management.base import BaseCommand
from app.models import Area

class Command(BaseCommand):
    help = 'Crea áreas manualmente'

    def handle(self, *args, **kwargs):
        areas = ['Frontend', 'Backend', 'Desarrollo de carrera', 'Diseño UX-UI', 'Freelancing',
                  'Introducción a la programación', 'Git', 'Inglés', 'Mobile', 'Orientación CV',
                  'QA', 'Product management', 'Soft skills']

        for area_name in areas:
            Area.objects.get_or_create(name=area_name)
            self.stdout.write(self.style.SUCCESS(f'Se creó la área: {area_name}'))

"""
---Para crearlos en el shell

python manage.py shell
from app.models import Area

areas = [
    'Frontend', 'Backend', 'Desarrollo de carrera', 'Diseño UX-UI', 'Freelancing',
    'Introducción a la programación', 'Git', 'Inglés', 'Mobile', 'Orientación CV',
    'QA', 'Product management', 'Soft skills'
]

for area_name in areas:
    Area.objects.get_or_create(name=area_name)

---Para verificar

from app.models import Area

areas = Area.objects.all()
for area in areas:
    print(area.name)

"""
