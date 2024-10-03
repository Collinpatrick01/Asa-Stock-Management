from django.urls import path
from lowbudget import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", views.signup, name="signup"),
    path("navbar/", views.navbar, name="navbar"),
    path("sidebar/", views.sidebar, name="sidebar"),
    path("footer/", views.footer, name="footer"),
    path("add-product/", views.add_product, name="add_product"),
    path("product-list/", views.product_list, name="product_list"),
    path("stock/", views.stock_list, name="stock_list"),
    path("sales/", views.perform_sales, name="perform_sales"),
    path("sales-list/", views.sales_list, name="sales_list"),
    path("edit-product/<int:product_id>/", views.edit_product, name="edit_product"),
    path(
        "delete-product/<int:product_id>/", views.delete_product, name="delete_product"
    ),
    # path('record-purchase/', views.purchase, name='record_purchase'),
    # Add other paths here
]
