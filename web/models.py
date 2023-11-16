from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    details=models.TextField()
    image=models.ImageField(upload_to='media')

    def __str__(self):
        return self.name
    

   