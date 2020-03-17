from django.contrib import admin
from .models import *

class GeneratorToCategory_inline(admin.TabularInline):
    model = GeneratorToCategory
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    inlines = (GeneratorToCategory_inline,)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Generator)
