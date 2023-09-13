from django.db import models

# Create your models here.

class Author(models.Model):
    firstname = models.CharField(max_length=225)
    lastname = models.CharField(max_length=225)
    description = models.TextField()
    date = models.DateField()
    phone = models.IntegerField()
    
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"