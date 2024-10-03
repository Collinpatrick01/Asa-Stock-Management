# forms.py

from django import forms
from .models import Product, Purchase

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_type', 'shelf_location', 'date_entered', 'quantity', 'unit', 'amount_cost']
        
        
        
class PurchaseForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), empty_label="Select Product")

    class Meta:
        model = Purchase
        fields = ['product', 'quantity', 'cost']