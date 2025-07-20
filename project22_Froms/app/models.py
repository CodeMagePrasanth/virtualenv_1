from django.db import models

# Create your models here.

class School(models.Model):
    Scname= models.CharField(max_length=100,primary_key=True)
    ScPrincipal = model.CharField(max_length=100)
    ScLoaction = models.CharField(max_length=100)

    def __str__(self):
        return self.School