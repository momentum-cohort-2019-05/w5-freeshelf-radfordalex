from django.contrib import admin
from core.models import Book
from core.models import Category

# Register your models here.

admin.site.register(Book)
admin.site.register(Category)
