from django.db import models

# Create your models here.
class Movie(models.Model):
    Name= models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField()
    img=models.ImageField(upload_to='images')

    def __str__(self):
        return self.Name
