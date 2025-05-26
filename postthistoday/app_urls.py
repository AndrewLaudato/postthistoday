from django.urls import path
from . import views

urlpatterns = [
    path('', views.writing_samples, name='writing_samples'),
]