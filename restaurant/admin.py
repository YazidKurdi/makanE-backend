from django.contrib import admin

from restaurant.models import FoodCategory, MenuItem

# Register your models here.
admin.site.register(FoodCategory)
admin.site.register(MenuItem)