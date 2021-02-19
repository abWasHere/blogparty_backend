"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path
<<<<<<< HEAD

from .views import api_homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_homepage, name='api_homepage'),
=======

urlpatterns = [
    path('admin/', admin.site.urls),
>>>>>>> eb4697e62c26c981de45a7670309b0d585f92542
    path('api/party/', include('party.urls'))
]
