from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Photo(models.Model):
    pic = models.ImageField(upload_to='pics')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

