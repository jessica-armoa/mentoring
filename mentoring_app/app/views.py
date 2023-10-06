from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from app.models import Area
from app.models import Mentor

from app.form import CustomUserCreationForm
from app.form import CustomMentorCreationForm

from django.http import JsonResponse
import requests

from django.contrib import messages

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


def calendar(request):
    if 'user_id' not in request.session:
            return redirect('login')

    user_in_session = None

    if 'user_id' in request.session:
        user_id = request.session['user_id']
        user_in_session = User.objects.filter(id=user_id).first()

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