from django.core import paginator
from django.shortcuts import render
from .models import Order, Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    products = Product.objects.all()
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        products = products.filter(title__icontains = item_name)

    paginator = Paginator(products, 4)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    
    return render(request, 'shop/index.html', {'products':products})

def detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'shop/detail.html', {'product':product})

def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items', "")
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        address = request.POST.get('address', "")
        city = request.POST.get('city', "")
        total = request.POST.get('total_price', "")

        order = Order(name=name, email=email, address=address, city=city, items=items, total=total)
        order.save()

    return render(request, 'shop/checkout.html')
