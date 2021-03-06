"""pizzaheaven URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin # default, provided
from django.urls import include, path
from pizza import views  # views from our local app ("pizza", for ordering pizza). Different views will be addressed as "object.attribute" scheme (e.g. "views.order")

urlpatterns = [
    path('admin/', admin.site.urls), # default, provided by Django
    path('', views.home, name='home'), # home route (e.g. "http://localhost:8000/")
    path('order/', include('pizza.urls')),
]
