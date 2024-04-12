from django.contrib import admin
from .models import TaskModel
from django.contrib.auth.admin import UserAdmin



# register FORMS



# MODEL REPRESENTATION IN ADMIN
class TaskModelAdmin(admin.ModelAdmin):
    model = TaskModel
    list_display = [
        'title', 
        'description', 
        'priority',
        'assigned_to',
        'due_date',
        'created_at', 
        'completed',

    ]
    list_filter = [
        'priority',
        'assigned_to',
        'due_date',
        'completed',
    ]
    #list_display = ('title', 'created_by', 'display_genre')
# def display_department(self):
#     """Create a string for the Genre. This is required to display genre in Admin."""
#     return ', '.join(title.name for title in self.TaskModel.all()[:3])

# display_department.short_description = 'Genre'

admin.site.register(TaskModel, TaskModelAdmin)