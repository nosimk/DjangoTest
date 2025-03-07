from django.db import models

# Create your models here.
class Person(models.Model):
    image = models.ImageField(upload_to='images/',blank=True)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.name