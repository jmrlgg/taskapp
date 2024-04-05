from django.contrib import admin
from django.contrib.auth import get_user_model #IMPORT MODEL
# user admin
from django.contrib.auth.admin import UserAdmin

# import forms
from .forms import CustomUserChangeForm, CustomUserCreationForm


# MODEL
CustomUser = get_user_model()

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'email', 
        'username', 
        'is_superuser', 
        'is_staff', 
        'is_active', 
        'date_joined'
        ]
    
# register FORMS
admin.site.register(CustomUser, CustomUserAdmin)