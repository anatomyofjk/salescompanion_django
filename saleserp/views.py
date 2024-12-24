from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import ProductCategory, Products, Inventory, Orders, Sales, Customers
from .forms import AddCategoryRecordForm, AddProductRecordForm, AddInventoryRecordForm, AddOrdersRecordForm, AddSalesRecordForm, AddCustomerRecordForm

##################################    Category Functions   ##################################################

def home(request):

    categories = ProductCategory.objects.raw("SELECT * FROM [dbo].[products_category]")
    # Validate user log in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    # authenticate
        user = authenticate(request, username = username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have Been Logged on")
            return redirect('home')
        else:
            messages.success(request, "Error")
            return redirect('home')
    else:
        return render(request, 'home.html', {'category': categories})


def category_record(request, pk):
    if request.user.is_authenticated:
        #look up record
        category_record = ProductCategory.objects.get(category_id=pk)
        return render(request, 'category_record.html', {'category_record':category_record})
    else:
        messages.success(request, "You must be logged in to view this page")
        return redirect('home')


def add_category_record(request):
    form = AddCategoryRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_category_record = form.save()
                messages.success(request, "Record Added")
                return redirect('home')
        return render(request,  'add_category_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged in to view this page")
        return redirect('home')


def update_category_record(request, pk):
    if request.user.is_authenticated:
        current_record = ProductCategory.objects.get(category_id=pk)
        form = AddCategoryRecordForm(request.POST or None, instance= current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated successfully")
            return redirect('home')
        return render(request,  'update_category_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged in to view this page")
        return redirect('home')

 
def delete_category_record(request, pk):
    if request.user.is_authenticated:
        delete_record = ProductCategory.objects.get(category_id=pk)
        delete_record.delete()
        messages.success(request, "Record deleted successfully")
        return redirect('home')
    else: 
        messages.success(request, "You must be logged in to view this page")
        return redirect('home')


##################################    Product Functions   ##################################################

def products(request):
    if request.user.is_authenticated:
        # categories = ProductCategory.objects.all()
        products = Products.objects.raw("SELECT * FROM [dbo].[products]")

    else:
        messages.success(request, "You must be logged in to view this page")
        return redirect('home')
    return render(request, 'products_home.html', {'products': products})


def product_record(request, pk):
    if request.user.is_authenticated:
        #look up record
        product_record = Products.objects.get(product_id=pk)
        return render(request, 'product_record.html', {'product_record':product_record})
    else:
        messages.success(request, "You must be logged in to view this page")
        return redirect('home')


def add_product_record(request):
    form = AddProductRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_product_record = form.save()
                messages.success(request, "Record Added")
                return redirect('home')
        return render(request,  'add_product_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged in to view this page")
        return redirect('home')

##################################    Inventory Functions   ##################################################

def inventory(request):
    if request.user.is_authenticated:
        inventories = Inventory.objects.raw("SELECT * FROM [dbo].[stock_control]")

    else:
        messages.success(request, "You must be logged in to view this page")
        return redirect('home')
    return render(request, 'inventory_home.html', {'inventories': inventories})


def inventory_record(request, pk):
    if request.user.is_authenticated:
        #look up record
        inventory_record = Inventory.objects.get(product_id=pk)
        return render(request, 'inventory_record.html', {'inventory_record':inventory_record})
    else:
        messages.success(request, "You must be logged in to view this page")
        return redirect('home')


def add_inventory_record(request):
    form = AddInventoryRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_inventory_record = form.save()
                messages.success(request, "Product added to inventory")
                return('inventory_home.html')
        return render(request, 'add_inventory_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged in to view this page")
        return redirect('home')



##################################    Orders Functions   ##################################################

def orders(request):
    if request.user.is_authenticated:
        orders = Orders.objects.all()
        return render(request, 'orders_home.html', {'orders':orders})
    else:
        return redirect('home')
    


def orders_record(request, pk):
    if request.user.is_authenticated:
        orders_record = Orders.objects.get(order_id=pk)
        return render(request, 'orders_record.html', {'orders_record': orders_record})
    else:
        messages.success(request, "You must be logged in to view this page")
        redirect('home')


def add_orders_record(request):
    form = AddOrdersRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_orders_record = form.save()
                messages.success(request, "Order added succesfully")
                return('orders_home.html')
        return render(request, 'add_orders_record.html', {'form': form})
    else:
        messages.success(request, "You must be logged in to view this page")
        return redirect('home')



##################################    Inventory Functions   ##################################################

def sales(request):
    sales = Sales.objects.all()
    if request.user.is_authenticated:
        return render(request, 'sales_home.html', {'sales':sales})
    else:
        messages.success(request, "You must be logged in to view this page")
        return redirect('home')


def sales_record(request, pk):
    if request.user.is_authenticated:
        sales_record = Sales.objects.get(sales_id = pk)
        return render(request, 'sales_record.html', {'sales_record':sales_record})
    else:
        messages.success(request, "You must be logged on to view this page")
        return redirect('home')


def add_sales_record(request):
    form = AddSalesRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_sales_record = form.save()
                messages.success(request, "Order added succesfully")
                return('sales_home.html')
        return render(request, 'add_product_sale_record.html', {'form': form})
    else:
        messages.success(request, "You must be logged in to view this page")
        return redirect('home')



##################################    Customers Functions   ##################################################

def customers(request):
    if request.user.is_authenticated:
        customers = Customers.objects.all()
        return render(request, 'customers_home.html', {'customers':customers})
    else:
        messages.success(request, "You must be logged in to view this page")
        return redirect('home')
    

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Customers.objects.get(customer_id=pk)
        return render(request, 'customer_record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You must be logged in to view this page")
        return redirect('home')
    

def add_customer_record(request):
    form = AddCustomerRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_customer_record = form.save()
                messages.success(request, 'Customer added successfully')
                return redirect('customers')
        return render(request, 'add_customer_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged in to view this page")
        return redirect('home')


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')
