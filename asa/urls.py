"""
URL configuration for asa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from lowbudget import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('navbar/', views.navbar, name='navbar'),
    path('sidebar/', views.sidebar, name='sidebar'),
    path('footer/', views.footer, name='footer'),
    path('add_product/', views.add_product, name='add_product'),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('product_list/', views.product_list, name='product_list'),
    path('stock/', views.stock_list, name='stock_list'),
    path('sales/', views.perform_sales, name='perform_sales'),
    path('sales_list/', views.sales_list, name='sales_list'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   # path('record_purchase/', views.purchase, name='record_purchase'),
    # Add other paths here
    
    
]
