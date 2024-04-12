
from django.forms import forms, ModelForm
from .models import TaskModel


class TaskCreationForm(ModelForm):
    
    class Meta:
        model = TaskModel
        fields = "__all__"
    

        
class TaskUpdateForm(ModelForm):
    
    class Meta:
        model = TaskModel
        exclude = ["assigned_by", "created_at", ]
        
