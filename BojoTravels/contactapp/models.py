from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    phone = models.CharField(max_length=20,null=True,blank=True)
    email = models.EmailField(max_length=255,null=True,blank=True)
    message = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name
   