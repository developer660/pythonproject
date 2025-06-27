from django.db import models

# Create your models here.
class personaldetail(models.Model):
    firstname = models.CharField(max_length=250)
    lastname=models.CharField(max_length=250)
    email=models.TextField()
    phonenumber=models.IntegerField()
    billingaddress=models.TextField()
    youraddress=models.TextField()
    state=models.TextField()
    district=models.TextField()
    subdistrict=models.TextField()
    def __str__(self):
        return self.name