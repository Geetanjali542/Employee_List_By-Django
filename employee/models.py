from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=300, blank=False, null=False)
    designation = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, blank=False)
    image = models.ImageField(upload_to = "images/")  #when images is defined it will automaticlly create the folder when the image will be uploaded from frontend
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name
    
    