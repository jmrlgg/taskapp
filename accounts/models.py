from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.





class CustomUser(AbstractUser):
    # cover_photo = models.ImageField(upload_to='covers/', null=True, blank=True)
    bio = models.CharField(max_length=255, blank=True)
    pass
