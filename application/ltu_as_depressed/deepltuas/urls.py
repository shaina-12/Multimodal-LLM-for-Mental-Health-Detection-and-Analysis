from django.urls import path
from . import views
from .views import upload_audio

urlpatterns = [
    path('', views.index, name='index'),
    path('upload-audio/', upload_audio, name='upload_audio'),
]
