from django.db import migrations, models

def create_areas(apps, schema_editor):
    Area = apps.get_model('app','Area')
    names = ["Frontend", "Backend", "Desarrollo de carrera", "Diseño UX-UI", "Freelancing", "Introducción a la Programación", "Git", "Inglés",
            "Mobile", "Orientación CV", "QA", "Product management", "Soft Skills"]
    areas = [Area(name=name) for name in names]
    Area.objects.bulk_create(areas)


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_areas)
    ]
