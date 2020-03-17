from django.db import models
from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    generators = serializers.SerializerMethodField()

    def get_generators(self, obj):
        serializer = GeneratorToCategorySerializer(obj.generatortocategory_set.all(), many=True)
        return serializer.data

    class Meta:
        model = Category
        fields = ['id', 'parent', 'title', 'description', 'generators']

class GeneratorToCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneratorToCategory
        fields = ['generator', 'label']
