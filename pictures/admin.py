from django.contrib import admin

# Register your models here.
from .models import Picture, Category

admin.site.register(Category)
admin.site.register(Picture)