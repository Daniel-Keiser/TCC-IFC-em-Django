"""almossom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main.views import (
    index, profile, events, about, event_edit, almo_edit, cadastro, cadastro_banda, galeria, programacao_almo,
    subscribe, unsubscribe, search
)

urlpatterns = [
    path('', index, name='index'),
    path('profile', profile, name='profile'),
    path('cadastro', cadastro, name='cadastro'),
    path('events', events, name='events'),
    path('galeria', galeria, name='galeria'),
    path('events/<int:id>/', event_edit, name='event_edit'),
    path('almossons/<int:id>', almo_edit, name='almo_edit'),
    path('almossons/<int:almo_id>/inscrever/<int:banda_id>', subscribe, name='subscribe'),
    path('almossons/<int:almo_id>/desinscrever/<int:banda_id>', unsubscribe, name='unsubscribe'),
    path('cadastro_banda', cadastro_banda, name='cadastro_banda'),
    path('programacao_banda', programacao_almo, name="programacao_banda"),
    path('about', about, name='about'),
    path('admin/', admin.site.urls),
    path('search/', search, name='search'),
    path('account/', include('django.contrib.auth.urls'))
]
