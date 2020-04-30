from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class REcipeManager(models.Manager):
    def get_high_rating_queryset(self):
        return super().get_queryset().filter(rating__gte=3)

    def get_null_queryset(self):
        return super().get_queryset().filter(description=None)


class Categories(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='user_categories')


class Recipe(models.Model):
    name = models.CharField(max_length=50, blank=True, default="No Name")
    categoryId = models.ForeignKey(Categories, on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    ingredients = models.TextField(blank=True, default="No ingredients")
    description = models.TextField(blank=True)
    rating = models.IntegerField(blank=True, null=True)
    image = models.TextField(blank=True)
    recipe_objects = REcipeManager()
    objects = models.Manager()