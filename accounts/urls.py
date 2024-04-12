from django.urls import path, reverse, include
from django.contrib import admin
from .views import home



urlpatterns = [
       
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    

]