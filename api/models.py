from django.db import models
from cloudinary.models import CloudinaryField



class Chocolate(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price=models.FloatField()
    rating=models.FloatField()
    origin=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    Chocolate = models.ForeignKey(Chocolate, related_name = 'ingredients', on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Media (models.Model):
    MEDIA_TYPE_CHOICES = [
        ('image','Image'),
        ('video', 'Video'),
    ]
    chocolate = models.ForeignKey(Chocolate,related_name='media', on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES)
    # file = models.FileField(upload_to='chocolates/') 
    file = CloudinaryField('file')
    
    def __str__(self):
        return f"{self.type} - {self.chocolate.name}"
    
class Quote(models.Model):
    chocolate =models.OneToOneField(Chocolate, related_name='quote', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"Quote for {self.chocolate.name}"
    