from django.urls import path

from . import views

urlpatterns = [
    path('run', views.run_model, name='run'),
    path('interface', views.interface, name='interface'),
]
