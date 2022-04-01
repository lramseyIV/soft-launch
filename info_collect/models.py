from django.db import models

# Create your models here.
class Lead (models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class AdminUser (models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)