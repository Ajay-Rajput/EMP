"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from setup import views
urlpatterns = [
     path('admin/', admin.site.urls),
    
     path('emp/', views.employee),#web page to add employee
     path('emsemp/', views.emsemp),#all employee 
     path('addemp/', views.addemployee,name='addemp'),# to add employee
     path('updateemp/<str:id>', views.updateemployee,name='updateemp'),# to update employee
     path('delemp/<str:id>', views.deleteemployee,name='delemp'),# to update employee
    
    
]
