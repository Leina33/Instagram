from django.db import models
#importing user method for django
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(default = 'default.jpg',upload_to = 'ProfilePicture/')
    bio = models.TextField(max_length = 25)
    date = models.DateTimeField(auto_now_add=True, null = True)
    
    def __str__(self):
        return f'{self.user.username} Profile'
        
        
    
class Image(models.Model):
    image = models.ImageField(upload_to='instagram/',null = 'False')
    caption = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    
    # def __str__(self):
    #     return self.caption
    
    # def save_image(self):
    #     self.save()
        @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return instagram
        
class Comments (models.Model):
    
    comment = models.CharField(max_length=150)
    author = models.ForeignKey('Profile',related_name='commenter' , on_delete=models.CASCADE)
    imagecomment = models.ForeignKey('Image', on_delete=models.CASCADE, related_name='image_comments')
    date = models.DateTimeField(auto_now_add=True)
    '''Method to filter database results'''
    def __str__(self):
        return self.author
    