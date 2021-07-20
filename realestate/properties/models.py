from django.db import models
from django.db.models.fields import TextField
from django.utils import timezone
# Create your models here.
class Homes(models.Model):
    house_name= models.CharField(max_length=50)
    address = models.TextField(max_length=255)
    date_added = models.DateTimeField(default=timezone.now)
    description = models.TextField()

    price = models.IntegerField()
    bedroom_amount = models.IntegerField()
    bathroom_amount = models.IntegerField()
    house_floor = models.IntegerField()
    garage_amount = models.IntegerField()
    square_feet = models.IntegerField()

    house_image = models.ImageField(upload_to = 'main_images')
    secondary_image = models.ImageField(upload_to = 'secondary_images')
