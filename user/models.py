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


class Basket(models.Model):
    id = models.UUIDField(default = uuid.uuid4, primary_key=True, unique=True, editable=False)
    costomer = models.ForeignKey(Costomer, related_name="Costomer", on_delete=models.CASCADE)
    praduct_id = models.ManyToManyField(Praduct, related_name='Praduct', blank=True)
    data = models.DateTimeField(auto_now_add=datetime.datetime.now())

    def __str__(self):
        return str(self.costomer)



