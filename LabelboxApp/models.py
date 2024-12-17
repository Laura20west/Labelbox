from django.db import models

# Create your models here.
class Album(models.Model):
 name = models.CharField(max_length=100)
 Job = models.CharField(max_length=100)# creates a foreign key to the 'Artists' table
 hotel_Main_Img = models.ImageField(upload_to='images/', default='SOME STRING')
 release_date = models.DateField()
