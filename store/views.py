from django.shortcuts import render

# Create your views here.
def store(request):
    return render(request, 'store/store.html')

def product_details(request):
    return render(request, 'store/product-detail.html')