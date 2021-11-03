from django.db import models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
import datetime
from django_group_by import GroupByMixin
from django.db.models.query import QuerySet


class ProductType(models.Model):
    category_name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return str(self.category_name)


class Store(models.Model):
    store_name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return str(self.store_name)


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    sale_price = models.IntegerField()
    image_url = models.CharField(max_length=150)

    def __str__(self):
        return str(self.product_name)

class Inventory(models.Model):
    """Inventory related data per product"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    units_available = models.IntegerField()
    product_like_count = models.IntegerField()
    product_reserve_count = models.IntegerField()
    arrival_date = models.DateField()

    def __str__(self):
        return str(self.product)


class UsersActionsQuerySet(QuerySet, GroupByMixin):
    pass


class UserAction(models.Model):
    objects = UsersActionsQuerySet.as_manager()


    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=50)
    user = models.CharField(max_length=100)
    date_time = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return str(self.user) + " " + str(self.action_type) + " " + str(self.product) + " from " + str(self.store) + " on " + str(self.date_time)



