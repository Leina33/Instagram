from django.db import models
#importing user method for django
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(default = 'default.jpg',upload_to = 'ProfilePicture/')
    
class Image(models.Model):
    image = models.ImageField(upload_to='instagram/',null = 'False')
    caption = models.CharField(max_length =500)
    
    def __str__(self):
        return self.caption