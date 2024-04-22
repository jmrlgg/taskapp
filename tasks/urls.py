"""
URL configuration for taskapp project.

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
from .views import hAPIView, TaskViewSet, SalesViewSet, HRViewSet, TaskList
from django.urls import include, path

# import routers 
from rest_framework import routers 
  

  
# define the router 
router = routers.DefaultRouter() 
  
# define the router path and viewset to be used 
router.register(r'task', TaskViewSet, basename="task")
router.register(r'sales', SalesViewSet, basename="sales") 
router.register(r'hr', HRViewSet, basename="hr") 
from .utils import getTaskList
# specify URL Path for rest_framework 
urlpatterns = [ 
    path('', include(router.urls)), 
    path('api-auth/', include('rest_framework.urls')),
    path('api/', hAPIView.as_view(), name='hello_world'),
    path('tasks/', getTaskList, name='routes'),
    path('ts/', TaskList.as_view(), name='')
]


