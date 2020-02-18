from ranshigen.models import Category
from ranshigen.serializers import CategorySerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['parent', 'title', 'description']


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
