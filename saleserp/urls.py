from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('categories/category_record/<int:pk>', views.category_record, name='category_record'),
    path('categories/add_category_record/', views.add_category_record, name='add_category_record'),
    path('categories/update_category_record/<int:pk>', views.update_category_record, name='update_category_record'),
    path('categories/delete_category_record/<int:pk>', views.delete_category_record, name='delete_category_record'),
    path('products', views.products, name='products'),
    path('products/product_record/<int:pk>', views.product_record, name='product_record'),
    path('products/add_product_record/', views.add_product_record, name='add_product_record'),
    path('inventory/', views.inventory, name='inventory'),
    path('inventory/inventory_record/<int:pk>', views.inventory_record, name='inventory_record'),
    path('inventory/add_inventory_record/', views.add_inventory_record, name='add_inventory_record'),
    path('orders/', views.orders, name='orders'),
    path('orders/orders_record/<int:pk>', views.orders_record, name='orders_record'),
    path('orders/add_orders_record', views.add_orders_record, name='add_orders_record'),
    path('sales/add_product_sale_record', views.add_sales_record, name='add_product_sale_record'),
    path('sales', views.sales, name='sales'),
    path('sales/sales_record/<int:pk>', views.sales_record, name='sales_record'),
    path('customers', views.customers, name='customers'),
    path('customers/view_customer_record/<int:pk>', views.customer_record, name='customer_record'),
    path('customers/add_customer', views.add_customer_record, name='add_customer_record'),
]