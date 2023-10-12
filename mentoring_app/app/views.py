from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from app.models import Availability, Meeting

from app.models import Area
from app.models import Mentor
from app.models import GoogleMeetRoom

from app.form import CustomUserCreationForm
from app.form import CustomMentorCreationForm
from app.form import CustomMeetingCreationForm

from django.http import JsonResponse, HttpResponse
import requests
from urllib.parse import urlencode

from django.contrib import messages

#Para el envio de correo
from django.core.mail import send_mail
from django.template.loader import render_to_string

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import os
#from google import Create_Service

from google.oauth2 import service_account
from googleapiclient.discovery import build

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from datetime import datetime, timedelta
import uuid


from zoomus import ZoomClient
import jwt
import time

def index(request):
    return redirect('login')

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        print(email, password)

        # Busca el usuario por su correo electrónico
        user = User.objects.filter(email=email).first()
        print(user.check_password(password))


        if user is not None and user.check_password(password):
            request.session['user_id'] = user.id
            messages.success(request, 'Sesión iniciada correctamente')

            mentors = Mentor.objects.all()
            all_user_id_mentors = [mentor.user_id for mentor in mentors]

            if user.id in all_user_id_mentors:
                request.session['is_mentor'] = True
                print("EL USER ES MENTOR")
                return redirect("/dashboard")
            else:
                request.session['is_mentor'] = False
                print("EL USER NO ES MENTOR")
                return redirect("/dashboard")
        else:
            messages.error(request, 'Correo electrónico o contraseña incorrectos')
            return redirect("login")

def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
        del request.session['is_mentor']
        messages.success(request, 'Sesión cerrada correctamente')
    return redirect("login")

def register_user(request):
    if request.method == "GET":
        return render(request, "register-user.html")
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print("*************** Usuario guardado:  " + user.email)
            messages.success(request, 'Usuario creado correctamente')
            return redirect('/login')
        else:
            errors = form.errors
            for e in errors:
                messages.error(request, e+" incorrecto, favor verifique sus datos.")
            return render(request, "register-user.html")

def register_mentor(request):
    if request.method == "GET":
        context = {'all_areas': Area.objects.all()}
        return render(request, "register-mentor.html", context)
    if request.method == "POST":
        form = CustomMentorCreationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
            )

            mentor = Mentor.objects.create(
                user=user,
                description=form.cleaned_data['description'],
                website=form.cleaned_data['website'],
                github=form.cleaned_data['github'],
                linkedin=form.cleaned_data['linkedin'],
            )

            mentor.areas.set(form.cleaned_data['areas'])

            # Iniciar sesión después de registrar
            user = User.objects.filter(email=request.POST['email']).first()

            if user is not None and user.check_password(request.POST['password1']):
                request.session['user_id'] = user.id
                mentors = Mentor.objects.all()
            all_user_id_mentors = [mentor.user_id for mentor in mentors]

            if user.id in all_user_id_mentors:
                request.session['is_mentor'] = True
                print("EL USER ES MENTOR")
                messages.success(request, 'Mentor creado correctamente')
                return redirect("/dashboard")#Aqui estaba la guia del mentor pero ya no vamos a usar por ahora
            else:
                request.session['is_mentor'] = False
                print("EL USER NO ES MENTOR")
                messages.success(request, 'Mentor creado correctamente')
                return redirect("/dashboard")
        else:
            errors = form.errors
            for e in errors:
                messages.error(request, e+" incorrecto, favor verifique sus datos.")
                context = {'all_areas': Area.objects.all(), 'form': form}
            return render(request, "register-mentor.html",context)


def guia_mentor(request):
    if 'user_id' not in request.session:
            return redirect('login')
    return render(request, "guia_mentor.html")

def edit_user(request, id):
    if 'user_id' not in request.session:
            return redirect('login')

    user = User.objects.filter(id=id).first()

    if request.method == 'GET':
        print("User a editar ", user.email)
        context = {'user': user}
        return render(request, "edit_user.html", context)

    if request.method == 'POST':
        new_first_name = request.POST.get('first_name')
        new_last_name = request.POST.get('last_name')
        new_username = request.POST.get('username')
        new_email = request.POST.get('email')
        new_password = request.POST.get('password1')

        # Actualizar first_name y last_name siempre
        user.first_name = new_first_name
        user.last_name = new_last_name

        # Actualizar username sin verificar si es único
        user.username = new_username

        # Actualizar email sin verificar si es único
        user.email = new_email

        # Actualizar contraseña solo si se proporciona una nueva y es diferente
        if new_password:
            user.set_password(new_password)

        user.save()

        messages.success(request, 'Los datos se han actualizado')
        return redirect('/dashboard')


def dashboard(request):
    if 'user_id' not in request.session:
            return redirect('login')

    user_in_session = None

    if 'user_id' in request.session:
        user_id = request.session['user_id']
        user_in_session = User.objects.filter(id=user_id).first()

    initials = None
    if user_in_session is not None:
        initials = user_in_session.first_name[:1].upper() + user_in_session.last_name[:1].upper()

    all_areas = Area.objects.all()
    all_mentors = Mentor.objects.all()

    if request.method == "GET":
        context = {
            'mentors': all_mentors,  # Cambiar a 'mentores' para que coincida con tu plantilla
            'all_areas': all_areas,
            'selected_area_id': int(request.GET.get('area_id')) if request.GET.get('area_id') else 0,
            'user_id': user_id,
            'is_mentor': request.session['is_mentor'],
            'user_in_session': user_in_session,
            'initials': initials,
        }
        return render(request, "dashboard.html", context)

    if request.method == "POST":
        print(request.POST)
        area_id = request.POST.get('area_id')

        if area_id != "0":
            mentors_filtrados = all_mentors.filter(areas__id=area_id)
        else:
            mentors_filtrados = Mentor.objects.all()

        context = {
            'mentors': mentors_filtrados,  # Cambiar a 'mentores' para que coincida con tu plantilla
            'all_areas': all_areas,
            'selected_area_id': int(area_id) if area_id else 0,
            'user_id': user_id,
            'user_in_session': user_in_session,
            'initials': initials,
        }

        return render(request, "dashboard.html", context)

def validate_calendly_username(request):
    username = request.GET.get('username')
    calendly_url = f'https://calendly.com/{username}'

    try:
        response = requests.get(calendly_url)
        response.raise_for_status()  # Esto generará una excepción si la respuesta no es 200 OK
        return JsonResponse({'valid': True})
    except requests.HTTPError:
        return JsonResponse({'valid': False})

def delete_user(request, id):
    user = User.objects.filter(id=id).first()
    print('ESTE ES EL ID DEL USUARIO A ELIMINAR', user.id)
    user.delete()
    logout(request)

    messages.success(request, 'La cuenta se ha eliminado correctamente')
    return redirect('/login')

def edit_mentor(request, id):
    if 'user_id' not in request.session:
            return redirect('login')

    user = User.objects.filter(id=id).first()
    mentor = Mentor.objects.get(user=user)

    if request.method == 'GET':
        print("User a editar ", user.email)

        mentor_areas = mentor.areas.all()
        context = {'user': user, 'all_areas': Area.objects.all(), 'mentor_areas': mentor_areas,}
        return render(request, "edit_mentor.html", context)

    if request.method == 'POST':
        new_first_name = request.POST.get('first_name')
        new_last_name = request.POST.get('last_name')
        new_username = request.POST.get('username')
        new_email = request.POST.get('email')
        new_password = request.POST.get('password1')

        # Actualizar first_name y last_name siempre
        user.first_name = new_first_name
        user.last_name = new_last_name

        # Actualizar username sin verificar si es único
        user.username = new_username

        # Actualizar email sin verificar si es único
        user.email = new_email

        # Actualizar contraseña solo si se proporciona una nueva y es diferente
        if new_password:
            user.set_password(new_password)

        user.save()

    # Actualiza los campos del mentor según sea necesario
        new_description = request.POST.get('description')
        new_linkedin = request.POST.get('linkedin')
        new_website = request.POST.get('web')
        new_github = request.POST.get('github')
    # Actualizar campos del modelo Mentor
        mentor.description = new_description
        mentor.linkedin = new_linkedin
        mentor.website = new_website
        mentor.github = new_github
    # Actualizar áreas seleccionadas
        selected_areas = request.POST.getlist('areas')  # Obtiene una lista de áreas seleccionadas
        mentor.areas.set(selected_areas)  # Actualiza las áreas asociadas al mentor

    # Guarda los cambios en el mentor
        mentor.save()


        # Redireccionar o hacer lo que necesites después de la actualización
        return redirect('/dashboard')


def calendar(request):
    if 'user_id' not in request.session:
            return redirect('login')

    user_in_session = None

    if 'user_id' in request.session:
        user_id = request.session['user_id']
        user_in_session = User.objects.filter(id=user_id).first()
        print("Usuario en sesion: ",user_in_session)

    initials = None
    if user_in_session is not None:
        initials = user_in_session.first_name[:1].upper() + user_in_session.last_name[:1].upper()

    if request.method == "GET":
        context = {
            'user_id': user_id,
            'user_in_session': user_in_session,
            'initials': initials,
        }
        return render(request, "calendar.html", context)


def user_calendar(request, mentor_id):

    user_in_session = None

    if 'user_id' in request.session:
        user_id = request.session['user_id']
        user_in_session = User.objects.filter(id=user_id).first()
        print("Usuario en sesion: ",user_in_session)

    initials = None
    if user_in_session is not None:
        initials = user_in_session.first_name[:1].upper() + user_in_session.last_name[:1].upper()

    mentor = Mentor.objects.get(pk=mentor_id)
    available_hours = Availability.objects.filter(mentor=mentor)

    if request.method == "GET":
        context = {
            'user_id': user_id,
            'user_in_session': user_in_session,
            'initials': initials,
            'mentor': mentor,
            'available_hours': available_hours
        }

        return render(request, 'calendar_user.html', context)

    if request.method == "POST":
        print(request.POST)
        form = CustomMeetingCreationForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            # Obtener el horario disponible seleccionado
            cleaned_data = form.clean()
            availability_id = cleaned_data.get('availability_id')
            description = cleaned_data.get('description')

            start = Availability.objects.get(id=availability_id)
            print(start)

            # Obtener una sala aleatoria no ocupada
            sala_disponible = GoogleMeetRoom.objects.filter(is_occupied=False).order_by('?').first()

            if sala_disponible:
                meeting = form.save(commit=False)
                meeting.room = sala_disponible
                meeting.description = description
                meeting.start = start
                meeting.user = user_in_session
                meeting.mentor = mentor

                correos = [user_in_session.email, mentor.user.email]
                print(".................",correos)

                meeting.save()
                print(meeting)
                start.is_available = False
                start.save()
                # Marcar la sala como ocupada
                sala_disponible.is_occupied = True
                sala_disponible.save()

                # Envía el correo después de guardar la mentoría
                asunto = "Mentoría gratuíta con Mentoring.dev"
                plantilla = "correo.html"
                contexto = {
                    'user': user_in_session,
                    'mentor': mentor,
                    'reunion': meeting,
                    'horario': start
                }
                mensaje = render_to_string(plantilla, contexto)
                enviar_correo(asunto, mensaje, mentor, user_in_session)

                messages.success(request, 'Revisa tu correo, te hemos mandado la información de la reunión')
                #190930802259-cuv3k92k38th8pqhebjhbug426vnths0.apps.googleusercontent.com
            else:
                messages.error(request, 'Lo sentimos, no tenemos salas disponibles, intente de nuevo más tarde')

            return redirect("/user/"+str(mentor_id)+"/calendar/")

def enviar_correo(asunto, mensaje, mentor, usuario):
    # Obtener las direcciones de correo del mentor y el usuario
    correo_mentor = mentor.user.email
    correo_usuario = usuario.email

    # Enviar correo
    send_mail(
        asunto,
        "",
        settings.EMAIL_HOST_USER,
        [correo_mentor, correo_usuario],
        html_message=mensaje,
        fail_silently=False,
    )

