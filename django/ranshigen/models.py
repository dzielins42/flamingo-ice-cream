from django.db import models
from ranshigen.generators import *

class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, default=None)
    title = models.CharField(max_length=128)
    description = models.TextField()
    # TODO image

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Generator(models.Model):
    id = models.CharField(primary_key=True, max_length=252, unique=True)
    data = models.TextField()

    def __str__(self):
        return self.id

    def generate(self, count=1):
        parser = XmlParser()
        generator = parser.fromString(str(self.data))
        return generator.generate(count)

    class Meta:
        verbose_name = 'Generator'
        verbose_name_plural = 'Generators'
