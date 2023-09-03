from django.db import models

# Create your models here.
class userdata(models.Model):
    name = models.CharField(max_length= 10)
    email = models.EmailField()
    dob = models.DateField()

    def __str__(self):
        return self.name
    
