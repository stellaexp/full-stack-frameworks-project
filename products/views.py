from django.shortcuts import render
from django.db import models


class Category(models.Model):
    name = models.Charfield(max_length=254)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
