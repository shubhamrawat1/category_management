from category.models import *
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'cat_name', 'created_date', 'cat_image', 'is_active']
