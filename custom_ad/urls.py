from django.urls import path
from . import views

app_name = 'custom_ad'

urlpatterns = [
    path('', views.custom_ad_index, name="custom_ad_index"),
]