from django.db import models
from ranshigen.generators import *

class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, default=None)
    title = models.CharField(max_length=128)
    description = models.TextField()
    image = models.ImageField(upload_to='categories', null=True, blank=True)
    generators = models.ManyToManyField('Generator', related_name='category', through='GeneratorToCategory')

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
        return generator.generate(count=count, referenceSolver=self._refSolver)

    def _refSolver(self, refId, count):
        return Generator.objects.get(id=refId).generate(count)

    class Meta:
        verbose_name = 'Generator'
        verbose_name_plural = 'Generators'

class GeneratorToCategory(models.Model):
    generator = models.ForeignKey('Generator', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    label = models.CharField(max_length=128)
