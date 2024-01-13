from django.db import models
import uuid

# # Create your models here.

class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Praduct(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=200)
    category_id = models.ForeignKey(Category, related_name='Category', on_delete=models.CASCADE)
    praduct_image = models.ImageField(upload_to='image/',default="/image/no-image.png", null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(default=0.0)
    existence = models.BooleanField(default=False)
 
    def __str__(self) -> str:
        return self.name
    


    
