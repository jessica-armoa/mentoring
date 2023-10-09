from django.db import migrations
from faker import Faker
from datetime import datetime, timedelta
from pytz import timezone
from django.contrib.auth.models import User


def create_mentor_with_defaults(apps, mentor_data=None):
    """
    Crea un mentor con datos predeterminados o personalizados.

    Args:
        apps: El objeto de aplicaciones Django.
        mentor_data (dict, optional): Un diccionario con los datos del mentor. Si no se proporciona,
            se usarán valores predeterminados generados aleatoriamente. Debe incluir los siguientes campos:
            - 'username' (str): Nombre de usuario.
            - 'email' (str): Dirección de correo electrónico.
            - 'password' (str): Contraseña.
            - 'description' (str): Descripción del mentor.
            - 'website' (str): URL del sitio web o portafolio del mentor.
            - 'github' (str): URL del perfil de GitHub del mentor.
            - 'linkedin' (str): URL del perfil de LinkedIn del mentor.
            - 'areas' (list, optional): Lista de IDs de áreas relacionadas con el mentor.
            - 'available_hours' (list, optional): Lista de IDs de horarios disponibles relacionados con el mentor.

    Returns:
        Mentor: El mentor creado.
    """

    Mentor = apps.get_model('app', 'Mentor')
    Availability = apps.get_model('app', 'Availability')
    Area = apps.get_model('app', 'Area')

    fake = Faker()  # Para generar datos aleatorios si es necesario

    # Si no se proporciona mentor_data, se utilizan valores predeterminados
    if mentor_data is None:
        mentor_data = {
            'username': 'default_username',
            'email': 'default_email@example.com',
            'password': 'default_password',
            'description': fake.text(),
            'website': fake.url(),
            'github': fake.url(),
            'linkedin': fake.url(),
            'areas': [],
            'available_hours': []
        }

    # Comprobar si el usuario ya existe
    user, created = User.objects.get_or_create(
        username=mentor_data['username'],
        defaults={'email': mentor_data['email']}
    )

    if created:
        user.set_password(mentor_data['password'])
        user.save()
        print(type(user))
        print(user)

    # Crear mentor
    mentor = Mentor(
        user=user,
        description=mentor_data['description'],
        website=mentor_data['website'],
        github=mentor_data['github'],
        linkedin=mentor_data['linkedin']
    )
    mentor.save()
    print(mentor)


    # Añadir áreas
    if not mentor_data['areas']:
        areas = Area.objects.all().order_by('?')[:4]  # Seleccionar 4 áreas al azar
        mentor.areas.set(areas)
    else:
        mentor.areas.set(mentor_data['areas'])

    # Añadir disponibilidades
    if not mentor_data['available_hours']:
        from datetime import datetime, timedelta
        today = datetime.now().date()
        for i in range(2):
            date = today + timedelta(days=i)
            for j in range(2):
                time_slot = datetime.combine(date, datetime.min.time()) + timedelta(hours=(10 + j))
                availability = Availability(hour=time_slot)
                availability.save()
                mentor.available_hours.add(availability)
    else:
        mentor.available_hours.set(mentor_data['available_hours'])

    return mentor


def create_mentors(apps, schema_editor):
    Availability = apps.get_model('app', 'Availability')

    asuncion = timezone('America/Asuncion')
    fmt = '%Y-%m-%d %H:%M:%S %Z%z'

    #Para la fecha
    today = datetime.now(asuncion)
    tomorrow = today + timedelta(days=1)  # Añade un día a la fecha actual

    #DATOS DE JESSICA
    horarios_jessica = [
        today.replace(hour=10, minute=00, second=0, microsecond=0),
        today.replace(hour=10, minute=30, second=0, microsecond=0),
        tomorrow.replace(hour=10, minute=30, second=0, microsecond=0),
    ]

    availability_jessica = [Availability(hour=horario) for horario in horarios_jessica]
    Availability.objects.bulk_create(availability_jessica)

    #Obtengo todos para luego buscar sus ids
    availabilities_created = Availability.objects.all()

    jessy_dict = {
        'username': 'jessyarmoa',
        'email': 'jessyarmoa@gmail.com',
        'password': '5381195Ja',
        'description': 'Estudiante de ingeniería y mentora con tres años de experiencia enseñando programación inicial, en python y C++, espero poder serte de mucha ayuda con las dudas que tengas :)',
        'website': '',
        'github': 'https://github.com/jessica-armoa',
        'linkedin': 'https://www.linkedin.com/in/jessica-armoa/',
        'areas': [1, 2, 6, 7],
        'available_hours': [availability.id for availability in availabilities_created]
    }

    mentor_jessy = create_mentor_with_defaults(apps, jessy_dict)
    print("Mentor creado ------>",mentor_jessy)

    #DATOS BRENDA
    horarios_brenda = [
        today.replace(hour=10, minute=30, second=0, microsecond=0),
        today.replace(hour=11, minute=00, second=0, microsecond=0),
        tomorrow.replace(hour=11, minute=30, second=0, microsecond=0),
    ]

    availability_brenda = [Availability(hour=horario) for horario in horarios_brenda]
    Availability.objects.bulk_create(availability_brenda)

    #Obtengo todos para luego buscar sus ids
    availabilities_created = Availability.objects.all()

    brenda_dict = {
        'username': 'brxndxz',
        'email': 'brendahuemer@gmail.com',
        'password': 'mariposas',
        'description': 'Full Stack Developer Python, programo con Django y Flask',
        'website': '',
        'github': 'https://github.com/jessica-armoa',
        'linkedin': 'https://www.linkedin.com/in/jessica-armoa/',
        'available_hours': [availability.id for availability in availabilities_created]
    }

    mentor_brenda = create_mentor_with_defaults(apps, brenda_dict)
    print("Mentor creado ------>",mentor_brenda)

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_areas'),
    ]

    operations = [
        migrations.RunPython(create_mentors)
    ]
