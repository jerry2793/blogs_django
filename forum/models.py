from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Posts(models.Model):
  user = models.ForegeinKey(User, models.CASCADE)
  title = models.CharField(max_length=500,blank=False)
  body = models.TextField(blank=False)
  
  
class Comments(models.Model):
  user = models.ForegeinKey(User, models.CASCADE)
  post = models.ForegeinKey(Post,models.CASCADE)
  body = models.TextField(blank=False)
  
  
class Replies(models.Model):
  user = models.ForegeinKey(User, models.CASCADE)
  comment = models.ForegeinKey(Comments,models.CASCADE)
  body= models.CharField(max_length=1000)
