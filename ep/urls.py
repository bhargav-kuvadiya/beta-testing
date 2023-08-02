from django.urls import path
from . import views

app_name = 'ep'

urlpatterns = [
    path('', views.ep_index, name="ep_index"),
]