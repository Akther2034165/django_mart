from django.shortcuts import render,get_object_or_404
from store.models import Product
from category.models import Category
def home(request, category_slug=None):
    searchItem = request.GET.get('searchItem')
    products = Product.objects.filter(is_available=True)

    if searchItem:
        products = products.filter(product_name__icontains=searchItem)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)


    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'home.html',context)

def nav_base(request, category_slug=None):
    searchItem = request.GET.get('searchItem')
    products = Product.objects.filter(is_available=True)

    if searchItem:
        products = products.filter(product_name__icontains=searchItem)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'base.html', context)