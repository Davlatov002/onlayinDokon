from django.db import models
import uuid, datetime
from shop.models import Praduct

class Costomer(models.Model):
    id = models.UUIDField(default = uuid.uuid4, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=255, null=True, blank=True)
    surname = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='image/',default="/image/default.jpg", null=True, blank=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.username
  
class Basket(models.Model):
    id = models.UUIDField(default = uuid.uuid4, primary_key=True, unique=True, editable=False)
    costomer = models.ForeignKey(Costomer, related_name="Costomer", on_delete=models.CASCADE)
    praduct_id = models.ManyToManyField(Praduct, related_name='Praduct', blank=True)
    price = models.FloatField(default=0.0)
    data = models.DateTimeField(auto_now_add=datetime.datetime.now())

    def __str__(self):
        return str(self.costomer.username)
    
    def save(self, *args, **kwargs): 
        total_price = sum(praduct.price for praduct in self.praduct_id.all())
        self.price = total_price
        super(Basket, self).save(*args, **kwargs)

class OrderProcess(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    basket_id = models.ForeignKey(Basket, related_name="Basket", on_delete=models.CASCADE)
    delivered = models.BooleanField(default=False)




 



