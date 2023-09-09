from django.shortcuts import render
from .models import Product
from category.models import Category
# Create your views here.
def store(request):
    products = Product.objects.filter(is_available = True)
    total_product = products.count()
    categories = Category.objects.all()
    return render(request, 'store/store.html', {'products':products, 'total_product':total_product, 'categories':categories})

def product_details(request):
    return render(request, 'store/product-detail.html')