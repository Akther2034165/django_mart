from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.core.paginator import Paginator

# def store(request, category_slug=None):
#     # Get the search query from the request GET parameters
#     searchItem = request.GET.get('searchItem')

#     # Start with a base queryset of all available products
#     products = Product.objects.filter(is_available=True)
#     # Filter products based on the search query, if provided
#     if searchItem:
#         products = products.filter(product_name__icontains=searchItem)

#     # Filter products based on the category, if provided
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category)
       
#     else:
#         products = Product.objects.filter(is_available=True)
        
#     paginator = Paginator(products, 3)
#     page = request.GET.get('page')
#     paged_product = paginator.get_page(page)    
#     categories = Category.objects.all()
    
#     context = {
#         'products': paged_product,
#         'categories': categories,
#     }
#     return render(request, 'store/store.html', context)

def store(request, category_slug=None):
    searchItem = request.GET.get('searchItem')
    products = Product.objects.filter(is_available=True)

    if searchItem:
        products = products.filter(product_name__icontains=searchItem)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    # Pagination
    paginator = Paginator(products, 3)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)
        
    categories = Category.objects.all()
    
    context = {
        'products': paged_product,
        'categories': categories,
    }
    return render(request, 'store/store.html', context)

def product_details(request, category_slug, product_slug):
    single_product = Product.objects.get(slug = product_slug, category__slug = category_slug)
    context = {
        'product': single_product
    }
    return render(request, 'store/product-detail.html', context)