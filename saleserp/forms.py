from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import ProductCategory, Products, Inventory, Orders, Sales, Customers

class AddCategoryRecordForm(forms.ModelForm):
    category_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"category name", "class":"form-control"}), label="")
    category_type = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"category type", "class":"form-control"}), label="")

    class Meta:
        model = ProductCategory
        exclude = ("user", )

class AddProductRecordForm(forms.ModelForm):
    product_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"product name", "class":"form-control"}), label="")
    product_description = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"product description", "class":"form-control"}), label="")
    year = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"year", "class":"form-control"}), label="")
    price = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"price", "class":"form-control"}), label="")

    class Meta:
        model = Products
        exclude = ("user", )

class AddInventoryRecordForm(forms.ModelForm):
    product_id = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"product id", "class":"form-control"}), label="")
    category_id = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"category id", "class":"form-control"}), label="")
    opening_stock = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"opening stock", "class":"form-control"}), label="")
    total_stock_sold = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"total stock sold", "class":"form-control"}), label="")
    remaining_stock = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"remaining stock", "class":"form-control"}), label="")

    class Meta:
        model = Inventory
        exclude = ("user", )

class AddOrdersRecordForm(forms.ModelForm):
    order_id = forms.IntegerField()
    quantity = forms.IntegerField()
    purchase_date = forms.DateTimeField()
    delivery_date = forms.DateTimeField()
    postage_fee = forms.FloatField()
    dealer = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"price", "class":"form-control"}), label="")

    class Meta:
        model = Orders
        exclude= ("user", )


class AddSalesRecordForm(forms.ModelForm):

    sales_id = forms.IntegerField()
    product_id = forms.IntegerField()
    category_id = forms.IntegerField()
    customer_id = forms.IntegerField()
    quantity = forms.FloatField()
    unit_price = forms.FloatField()
    total = forms.FloatField()
    time_of_sale = forms.DateTimeField()

    class Meta:
        model = Sales
        exclude = ("user", )


class AddCustomerRecordForm(forms.ModelForm):
    customer_id = forms.IntegerField()
    firstname = forms.CharField(max_length=50)
    middle_name = forms.CharField(max_length=50)
    lastname = forms.CharField(max_length=50)
    gender = forms.CharField(max_length=1)
    age = forms.IntegerField()
    mobile_number = forms.CharField(max_length=15)
    address = forms.CharField(max_length=150)
    occupation = forms.CharField(max_length=50)

    class Meta:
        model = Customers
        exclude = ("user", )
