"""Users forms."""

# Django
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone

# Otros
from datetime import datetime, timedelta, time

# Models
from django.contrib.auth.models import User
from app.models import Area
from app.models import Meeting
from app.models import Availability


class CustomUserCreationForm(UserCreationForm):
    """
    El modelo de formulario de creación de usuario personalizado.
    Este modelo herea de UserCreationForm y agrega un campo de correo
    electrónico.

    Args:
        UserCreationForm (UserCreationForm): Formulario de creación de usuario
        de Django.

    Returns:
        User: Modelo de usuario de Django.
    """

    username = forms.CharField(max_length=30, required=True, help_text='Por favor, ingresa un nombre de usuario válido.')
    email = forms.EmailField(required=True)
    help_texts = {
            'first_name': 'Por favor, ingresa un nombre válido, debe tener al menos 3 letras.',
            'last_name': 'Por favor, ingresa un apellido válido, debe tener al menos 3 letras.',
            'email': 'Por favor, ingresa una dirección de correo válida.',
            'password1': 'Por favor, completa el campo "contraseña", debe tener al menos 8 caracteres.',
            'password2': 'Por favor, completa el campo "confirme contraseña", debe coincidir con "contraseña".',
        }

    class Meta:
        """Meta options."""

        model = User
        fields = ('username', "first_name", "last_name", "email", "password1", "password2")


    def save(self, commit=True):
        """Save form."""

        user = super(CustomUserCreationForm, self).save(commit=False)
        user.username = self.cleaned_data["username"]
        user.email = self.cleaned_data["email"]
        print("********************************"+self.cleaned_data["username"])


        if commit:
            user.save()
        return user

    def clean_email(self):
        """Clean email."""

        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists(): #VER MENSAJES
            raise forms.ValidationError(message="El correo ya existe, intente con otro")
        return email


class CustomMentorCreationForm(forms.ModelForm):
    """Formulario de creación de mentor personalizado."""

    # Agregar campos específicos de Mentor
    description = forms.CharField(max_length=500, required=True)
    website = forms.URLField(required=False)
    github = forms.URLField(required=False)
    linkedin = forms.URLField(required=False)
    areas = forms.ModelMultipleChoiceField(
        queryset=Area.objects.all(),  # Esto obtiene todas las áreas disponibles
        widget=forms.CheckboxSelectMultiple,  # Esto renderiza las opciones como checkboxes
        required=True,  # Opcional, dependiendo de tus requisitos
        help_text='Selecciona las áreas en las que deseas ayudar.'  # Texto de ayuda
    )

    # Campos del usuario
    username = forms.CharField(max_length=30, required=True, help_text='Por favor, ingresa un nombre de usuario válido.')
    first_name = forms.CharField(max_length=30, required=True, help_text='Por favor, ingresa un nombre válido, debe tener al menos 3 letras.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Por favor, ingresa un apellido válido, debe tener al menos 3 letras.')
    email = forms.EmailField(required=True, help_text='Por favor, ingresa una dirección de correo válida.')
    password1 = forms.CharField(widget=forms.PasswordInput, required=True, help_text='Por favor, completa el campo "contraseña", debe tener al menos 8 caracteres.')
    password2 = forms.CharField(widget=forms.PasswordInput, required=True, help_text='Por favor, completa el campo "confirme contraseña", debe coincidir con "contraseña".')

    help_texts = {
        'email': 'Por favor, ingresa una dirección de correo válida.',
        'description': 'Por favor, proporciona una descripción.',
        'website': 'Por favor, ingresa una URL válida.',
        'github': 'Por favor, ingresa una URL válida.',
        'linkedin': 'Por favor, ingresa una URL válida.',
    }

    def clean_areas(self):
        areas = self.cleaned_data.get('areas')
        if not areas:
            raise forms.ValidationError("Debes seleccionar al menos un área.")
        return areas

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2', 'areas']

    def clean_email(self):
        """Clean email."""

        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(message="El correo ya existe, intente con otro")
        return self.cleaned_data["email"]


class AvailabilityForm(forms.Form):
    selected_date = forms.DateField()
    hour_start = forms.TimeField()  
    hour_end = forms.TimeField()  
    def clean(self):
            cleaned_data = super().clean()
            selected_date = cleaned_data.get('selected_date')
            hour_start = cleaned_data.get('hour_start')
            hour_end = cleaned_data.get('hour_end')
            
            if selected_date and hour_start and hour_end:
                # Calcula el end como media hora después del start
                end = time(hour_end.hour, (hour_end.minute // 30) * 30)  # Redondea a la media hora
                start = time(hour_start.hour, (hour_start.minute // 30) * 30)  # Redondea a la media hora
                
                # Crea una lista de horarios de 30 minutos entre start y end
                times = []
                current_time = start
                while current_time < end:
                    times.append(current_time)
                    current_time = (datetime.combine(datetime.min, current_time) + timedelta(minutes=30)).time()
                
                # Combina la fecha y la hora para crear objetos datetime
                datetime_values = [datetime.combine(selected_date, t) for t in times]
                
                return datetime_values

            raise forms.ValidationError("Ambos campos de fecha y hora son requeridos.")


class CustomMeetingCreationForm(forms.ModelForm):
    availability_id = forms.IntegerField()
    description = forms.CharField(max_length=500, required=True)

    class Meta:
        model = Meeting
        fields = ['availability_id', 'description']

    def save(self, commit=True):
        meeting = super().save(commit=False)

        if commit:
            meeting.save()
        return meeting

