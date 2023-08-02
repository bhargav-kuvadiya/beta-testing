"""beta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls', namespace='beta_dashboard')),
    path('blog/', include('blog.urls', namespace='beta_blog')),
    path('custom_ad/', include('custom_ad.urls', namespace='beta_custom_ad')),
    path('ep/', include('ep.urls', namespace='beta_ep')),
    path('it/', include('it.urls', namespace='beta_it')),
    path('projects/', include('projects.urls', namespace='beta_projects')),
    path('sit/', include('sit.urls', namespace='beta_sit')),

]
