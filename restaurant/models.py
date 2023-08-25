from django.db import models

class FoodCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE,related_name="menu_items")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name
