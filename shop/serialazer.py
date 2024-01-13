from rest_framework import serializers
from .models import Praduct, Category

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class CreateCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)

class UpdateCategorySerialazer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)



class Praductserializers(serializers.ModelSerializer):
    class Meta:
        model = Praduct
        fields = "__all__"

class CreatePraductserializers(serializers.ModelSerializer):
    class Meta:
        model = Praduct
        fields = ('name', 'category_id','description', 'price', 'existence')

class UpdatePraductserialazer(serializers.ModelSerializer):
    class Meta:
        model = Praduct
        fields = ('name','description','price','existence')

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.price = validated_data.get("price", instance.price)
        instance.existence = validated_data.get("existence", instance.existence)

class SearchPraductserializers(serializers.Serializer):
    search = serializers.CharField()