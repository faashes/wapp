

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home', views.home, name='home'),
    path('send', views.send),
    path('sendfromcsv', views.sendfromcsv),
    path('admin/', admin.site.urls),
]
