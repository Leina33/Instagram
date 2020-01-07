from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='instagram/',null = 'False')
    caption = models.CharField(max_length =500)
    
    def __str__(self):
        return self.caption