from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone= models.CharField(max_length=50)
    desc = models.TextField()
    date = models.DateField()   

    def __str__(self) -> str:
        return self.name


class emailSubscribe(models.Model):
    email = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.email