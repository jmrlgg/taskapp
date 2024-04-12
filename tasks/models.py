from django.db import models

# Create your models here.

class TaskModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=255, blank=True, null=True)
    priority = models.CharField(max_length=255, blank=True, null=True)
    completed = models.BooleanField(default=False)
    assigned_to = models.ForeignKey('accounts.CustomUser', on_delete=models.SET_NULL, null=True, blank=True)

    def __unicode__(self):
        return self.title
    
    def report_model_name(self, instance):
        short_description = 'Task Model Management'
#TODO: TASK MODEL TO FINSIH
    #updated_at = models.DateTimeField(auto_now=True)
    #completed_at = models.DateTimeField(blank=True, null=True)
    #completed_by = models.ForeignKey('accounts.CustomUser', on_delete=models.SET_NULL, null=True, blank=True)
    #assigned_to = models.ForeignKey('accounts.CustomUser', on_delete=models.SET_NULL, null=True, blank=True)
    #assigned_by = models.ForeignKey('accounts.CustomUser', on_delete=models.SET_NULL, null=True, blank=True)
    #TODO:Project/Department Model
    #project = models.ForeignKey('projects.ProjectModel', on_delete=models.SET_NULL, null=True, blank=True)
    #parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    #children = models.ManyToManyField('self', blank=True, related_name='children')


    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        