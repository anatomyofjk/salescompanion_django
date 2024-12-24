from django.db import models
from django.urls import reverse

class ProductCategory(models.Model):
    category_id = models.IntegerField(primary_key=True, unique=True, editable=False)
    category_name = models.CharField(max_length=50)
    category_type = models.CharField(max_length=20)
    creation_date = models.DateTimeField(editable=True, auto_now_add=True)
    # last_updated_date = models.DateTimeField(editable=True, auto_now=True)
    objects = models.Manager() # The default Manager
    

    class Meta:
        verbose_name_plural = "Product Category"
        db_table = "[dbo].[products_category]"

    def get_absolute_url(self):
        return reverse('saleserp:viewProductCategory', args=[self.categoty_id])

class Products(models.Model):
    product_id = models.IntegerField(primary_key=True, editable=False, unique=True)
    product_name  = models.CharField(max_length=50)
    product_description = models.CharField(max_length=255)
    category_id = models.IntegerField(editable=False)
    year = models.DateField(editable=True)
    price = models.FloatField()
    creation_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    last_updated_user = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Product"
        db_table = "[dbo].[products]"

    
class Inventory(models.Model):
    product_name = models.CharField(max_length=50)
    product_description = models.CharField(max_length=50)
    product_id = models.IntegerField(primary_key=True, editable=False, unique=True)
    category_id = models.IntegerField(editable=False)
    opening_stock = models.IntegerField()
    total_stock_sold = models.IntegerField()
    remaining_stock = models.IntegerField()
    creation_date = models.DateTimeField()
    last_date_updated = models.DateTimeField()
    last_updated_user = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Inventory"
        db_table = "[dbo].[stock_control]"

class Orders(models.Model):
    order_id = models.IntegerField(primary_key=True)
    quantity = models.IntegerField()
    purchase_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    postage_fee = models.FloatField()
    dealer = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Order"
        db_table = "[dbo].[orders]"


class Sales(models.Model):
      sales_id = models.IntegerField(primary_key=True)
      product_id = models.IntegerField()
      category_id = models.IntegerField()
      customer_id = models.IntegerField()
      quantity = models.IntegerField()
      unit_price = models.FloatField()
      total = models.FloatField()
      time_of_sale = models.DateTimeField()

      class Meta:
          verbose_name_plural = "Sales"
          db_table = "[dbo].[sales]"

class Customers(models.Model):
    
    customer_id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=1)
    age = models.IntegerField()
    mobile_number = models.CharField(max_length=15)
    address = models.CharField(max_length=150)
    occupation = models.CharField(max_length=50)
    creation_date = models.DateTimeField()
    last_updated = models.DateTimeField()

    class Meta:
        db_table = "[dbo].[customers]"