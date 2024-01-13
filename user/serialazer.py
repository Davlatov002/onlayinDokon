from rest_framework import serializers
from .models import Costomer, Basket

class BaskerSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = "__all__"

class CreateBaskerSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ("costomer","praduct_id")

class CostomerSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Costomer
        fields = "__all__"

class CreateCostomerSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Costomer
        fields = ("username", "email", "password")

class UpdateCostomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Costomer
        fields = ('name','surname','image','username', "password", "email")

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.surname = validated_data.get("surname", instance.surname)
        instance.image = validated_data.get("image", instance.image)
        instance.username = validated_data.get("username", instance.username)
        instance.password = validated_data.get("password", instance.password)
        instance.email = validated_data.get("email", instance.email)


