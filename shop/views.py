from django.shortcuts import render
from .models import Product
from math import ceil
# Create your views here.
def index(request):
    # products = Product.objects.all()

    allprods = []
    catprods = Product.objects.values("category")
    cats = {item['category'] for item in catprods}

    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nslides = n//4 + ceil(n/4 - (n//4))
        allprods.append([prod , range(1,nslides),nslides])
        
    params = {
        "allprods":allprods
    }
    return render(request, "index.html",params)


def product_view(request, id ):
    products = Product.objects.filter(id = id)
    
    return render(request, "product_page.html",{"product":products[0]})