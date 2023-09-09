from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def store(request, category_slug=None):
    # Get the search query from the request GET parameters
    searchItem = request.GET.get('searchItem')

    # Start with a base queryset of all available products
    products = Product.objects.filter(is_available=True)

    # Filter products based on the search query, if provided
    if searchItem:
        products = products.filter(product_name__icontains=searchItem)

    # Filter products based on the category, if provided
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    total_product = products.count()
    categories = Category.objects.all()
    context = {
        'products': products,
        'total_product': total_product,
        'categories': categories,
    }
    return render(request, 'store/store.html', context)


def product_details(request):
    return render(request, 'store/product-detail.html')