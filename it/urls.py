from django.urls import path
from . import views

app_name = 'it'

urlpatterns = [
    path('', views.it_index, name="it_index"),
]