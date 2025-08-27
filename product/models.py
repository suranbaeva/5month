from django.db import models
from django.db.models import TextField


class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.title

STAR_CHOICES = (
    (i, '*' * i) for i in range(1,6)
)

class Review(models.Model):
    text = TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stars = models.IntegerField(default=5, choices=STAR_CHOICES)

    def __str__(self):
        return (f'Отзыв к продукту {self.product}')



