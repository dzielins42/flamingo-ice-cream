from ranshigen.models import Category, Generator
from ranshigen.serializers import CategorySerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'parent': ['exact', 'isnull'],
        'title':['exact'],
        'description':['exact']
    }

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class GeneratorResults(APIView):
    def get(self, request, id, format=None):
        try:
            generator = Generator.objects.get(id=id)
        except Generator.DoesNotExist:
            raise Http404
        count = int(request.query_params.get(key='count', default=10))
        result = generator.generate(count)
        return Response(result)
