from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .models import Product
from .forms import ProductForm, PurchaseForm
from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q


@login_required
def index(request):
    recent_products = Product.objects.all()
    total_products = recent_products.count()
    total_amount = recent_products.aggregate(Sum('amount_cost'))['amount_cost__sum']
    
    product_names = [product.product_name for product in recent_products]
    product_quantities = [product.quantity for product in recent_products]
    
    
    context = {
        'recent_products': recent_products,
        'total_products': total_products,  # Pass the total number of products to the template
        'product_name': 'Product Name',
        'product_type': 'Product Type',
        'total_amount': total_amount,
        
        'product_names': product_names,
        'product_quantities': product_quantities,
    }
    return render(request, 'index.html', context)

def login_view(request):
    return auth_views.LoginView.as_view(template_name='login.html')(request)


def signup(request):
    return render(request, 'signup.html')

def sidebar(request):
    return render(request, '_sidebar.html')

def navbar(request):
    return render(request, '_navbar.html')

def footer(request):
    return render(request, '_footer.html')

@login_required
def add_product(request):
    if request.method == 'POST':
        product_name = request.POST['product_name']
        product_type = request.POST['product_type']
        shelf_location = request.POST['shelf_location']
        date_entered = request.POST['date_entered']
        quantity = request.POST['quantity']
        amount = request.POST['amount']
        unit = request.POST['unit']
        Product.objects.create(
            product_name=product_name,
            product_type=product_type,
            shelf_location=shelf_location,
            date_entered=date_entered,
            quantity=quantity,
            unit=unit,
        )
        return redirect('product_list')
    return render(request, 'add_product.html')


def product_list(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(
            Q(product_name__icontains=query) | Q(product_type__icontains=query)
        )
    else:
        products = Product.objects.all()
    
    context = {
        'products': products,
    }
    return render(request, 'product_list.html', context)

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form})

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'delete_product.html', {'product': product})


@login_required
def stock_list(request):
    products = Product.objects.all()
    return render(request, 'stock.html', {'products': products})


@login_required
def perform_sales(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        quantity = int(request.POST['quantity'])
        date_of_sales = request.POST['date_of_sales']
        total_amount = float(request.POST['total_amount'])

        # Update the product quantity in the database
        product = Product.objects.get(id=product_id)
        if product.quantity >= quantity:
            try:
                # Save the sales record
                Sales.objects.create(product=product, quantity=quantity, date_of_sales=date_of_sales, total_amount=total_amount)
                product.quantity -= quantity
                product.save()
                return redirect('perform_sales')
            except ValidationError as e:
                return render(request, 'sales.html', {
                    'products': Product.objects.all(),
                    'sales': Sales.objects.all(),
                    'error': e.message
                })
        else:
            return render(request, 'sales.html', {
                'products': Product.objects.all(),
                'sales': Sales.objects.all(),
                'error': 'Insufficient stock'
            })

    return render(request, 'sales.html', {
        'products': Product.objects.all(),
        'sales': Sales.objects.all()
    })


@login_required
def sales_list(request):
    sales = Sales.objects.all()
    return render(request, 'sales_list.html', {'sales': sales})


@login_required
def record_purchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            purchase = form.save()
            # Update the product stock
            product = purchase.product
            product.quantity += purchase.quantity
            product.save()
            return redirect('purchase_list')
    else:
        form = PurchaseForm()
    return render(request, 'purchase.html', {'form': form})
# Create your views here.
# <form method="POST" action="{% url 'logout' %}">
    #            {% csrf_token %}
    #            <button type="submit" class="dropdown-item">
    #              <i class="ti-power-off text-primary"></i>
    #              Logout
     #           </button>
      #        </form>