from django.urls import path

from . import views

urlpatterns = [
    path('run', views.run_model, name='run'),
    path('show_result', views.show_result, name='show_result'),
    path('upload', views.upload_file, name='upload'),
    path('', views.home, name='home'),
    path('loading', views.loading, name='loading'),
    path('download/<int:filenum>', views.download, name='download'),
]
