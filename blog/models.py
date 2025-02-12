from django.db import models

# Create your models here.

#model for writing post
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']


#model for user registration 
class UserRegistration(models.Model):
    username = models.CharField(max_length=225)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=225)
    confirm_password = models.CharField(max_length=225)
