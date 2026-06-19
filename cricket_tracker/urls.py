from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path(
        'admin/',
        admin.site.urls
    ),

    path(
        '',
        include('dashboard.urls')
    ),

    path(
        'players/',
        include('players.urls')
    ),

    path(
    'matches/',
    include('matches.urls')
),

    path(
    'api/',
    include('api.urls')
    ),

     path(
    'tournaments/',
    include('tournaments.urls')
    ),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )