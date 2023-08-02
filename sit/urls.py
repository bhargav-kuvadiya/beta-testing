from django.urls import path
from . import views

app_name = 'sit'

urlpatterns = [
    path('', views.sit_index, name="sit_index"),
]