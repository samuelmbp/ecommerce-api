from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Customer, Collection, Order, OrderItem

# NOTE: Every models class has a manager 'objects'


def say_hello(request):
    # NOTE: Retrieving Objects
    # exists = Product.objects.filter(pk=0).exists()

    # NOTE: Filtering Objects
    # queryset = Product.objects.filter(unit_price__gt=20)
    # queryset = Product.objects.filter(unit_price__range=(20, 30))
    # queryset = Product.objects.filter(title__icontains='coffee')
    # queryset = Product.objects.filter(last_update__year=2021)
    # queryset = Product.objects.filter(description__isnull=True)

    # Filtering Exercise:
    # 1. Customers with .com accounts
    # queryset = Customer.objects.filter(email__icontains='.com')

    # 2. Collections that don’t have a featured product
    # queryset = Collection.objects.filter(featured_product__isnull=True)

    # 3. Products with low inventory (less than 10)
    # queryset = Product.objects.filter(inventory__lt=10)

    # 4. Orders placed by customers with id=1
    # queryset = Order.objects.filter(customer__id=1)

    # 5. Order items for products in collection 3
    # queryset = OrderItem.objects.filter(product__collection__id=3)

    return render(request, 'hello.html', {'name': 'Samuel', 'products': list(queryset)})
