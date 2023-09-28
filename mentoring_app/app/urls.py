from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register/user', views.register_user),
    path('edit/user/<int:id>', views.edit_user),
    path('register/mentor', views.register_mentor),
    path('guia/mentor', views.guia_mentor),
    path('dashboard', views.dashboard),
    path('validate_calendly_username/', views.validate_calendly_username, name='validate_calendly_username'),
]