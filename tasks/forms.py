
from django.forms import forms, ModelForm
from .models import TaskModel

#Create TaskModel Form Recieve
class TaskCreationForm(ModelForm):
    
    class Meta:
        model = TaskModel
        fields = "__all__"
    

       # UPDATE TASK MODEL
class TaskUpdateForm(ModelForm):
    
    class Meta:
        model = TaskModel
        exclude = ["assigned_by", "created_at", ]
        
