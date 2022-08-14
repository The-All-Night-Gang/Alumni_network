from django.contrib import admin

# Register your models here.
from feed.models import Photo, Category

admin.site.register(Category)
admin.site.register(Photo)
