from rest_framework import serializers
from .models import FoodCategory, MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['name', 'price', 'description', 'image']

class FoodCategorySerializer(serializers.ModelSerializer):
    menu_items= MenuItemSerializer(many=True, read_only=True)

    class Meta:
        model = FoodCategory
        fields = ['name', 'menu_items']
