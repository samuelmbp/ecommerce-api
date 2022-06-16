from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Min, Max, Avg, Sum
from store.models import Product, Customer, Collection, Order, OrderItem

# NOTE: Every models class has a manager 'objects'


def say_hello(request):
    # NOTE: Retrieving Objects
    # exists = Product.objects.filter(pk=0).exists()

    # =============================================
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

    # =============================================
    # NOTE: Complex Lookups using Q objects
    # queryset = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20) # AND
    # queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20)) # OR

    # =============================================
    # NOTE: Referencing Fields using F objects
    # queryset = Product.objects.filter(inventory=F('unit_price'))
    # queryset = Product.objects.filter(inventory=F('collection__id'))

    # =============================================
    # NOTE: Sorting Data
    # queryset = Product.objects.order_by('title') # A - Z
    # queryset = Product.objects.order_by('-title') # Z - A
    # product = Product.objects.order_by('unit_price')[0]
    # product = Product.objects.earliest('unit_price') # Returns an object
    # product = Product.objects.latest('unit_price')

    # =============================================
    # NOTE: Limiting Results
    # queryset = Product.objects.all()[:5]  # 0, 1, 2, 3, 4
    # queryset = Product.objects.all()[5:10]  # 5, 6, 7, 8, 9

    # =============================================
    # NOTE: Selecting Fields to Query
    # queryset = Product.objects.values('id', 'title') # returns key-value pairs (dictionaries)
    # queryset = Product.objects.values(
    # 'id', 'title', 'collection__id')  # Joint query
    # queryset = Product.objects.values_list('id', 'title')  # returns tuples

    # Exercise:
    # - select products that have been ordered and sort them by title

    # queryset = Product.objects.filter(id__in=OrderItem.objects.values(
    #     'product__id').distinct()).order_by('title')  # distinct = no duplication

    # =============================================
    # NOTE: Deferring Fields
    # Returns instances of the product class
    # queryset = Product.objects.only('id', 'title', 'unit_price')
    # all fields except description
    # queryset = Product.objects.defer('description')

    # =============================================
    # NOTE: Selecting Related Objects
    # queryset = Product.objects.select_related('collection').all() # Product has one relation (to collection)
    # queryset = Product.objects.prefetch_related(
    #     'promotions').all()  # Product has many relations (Promotion)

    # Complex query
    # queryset = Product.objects.prefetch_related(
    #     'promotions').select_related('collection').all()

    # Exercise
    # queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]

    # =============================================
    # NOTE: Aggregating Objects
    # result = Product.objects.aggregate(
    #     count=Count('id'), min_price=Min('unit_price'))

    # Exercises
    # 1. How many orders do we have?
    # result = Order.objects.aggregate(order_count=Count('id'))

    # 2. How many units of product 1 have we sold?
    # result = OrderItem.objects \
    #     .filter(product__id=1) \
    #     .aggregate(units_sold=Sum('quantity'))

    # 3. How many orders has customer 1 placed?
    # result = Order.objects.filter(customer__id=1).aggregate(count=Count('id'))

    # 4. What is the min, max and average price of the products in collection 3?
    # result = Product.objects.filter(collection__id=3) \
    #     .aggregate(
    #         min_price=Min('unit_price'),
    #         max_price=Max('unit_price'),
    #         avg_price=Avg('unit_price')
    # )

    # =============================================
    # NOTE: Annotating Objects = adding additional attributes/fields while querying
    # queryset = Customer.objects.annotate(is_new=Value(True)) # is_new becomes a field in the db
    # queryset = Customer.objects.annotate(new_id=F('id')) # Increases from 1..1000

    # =============================================
    # NOTE: Calling DB Functions
    # queryset = Customer.objects.annotate(
    #     full_name=Func(F('first_name'), Value(
    #         ' '), ('last_name'), function='CONCAT')
    # )
    # Shorter and cleaner with Concat
    # queryset = Customer.objects.annotate(
    #     full_name=Concat('first_name', Value(' '), 'last_name'))

    # =============================================
    # NOTE: Grouping Data
    # queryset = Customer.objects.annotate(orders_count=Count('order'))

    # =============================================
    # NOTE: Expression Wrappers - Complex Expressions
    # discounted_price = ExpressionWrapper(
    #     F('unit_price') * 0.8, output_field=DecimalField())

    # queryset = Product.objects.annotate(discounted_price=discounted_price)

    # Exercises
    # 1. Customers with their last order id
    # queryset = Customer.objects.annotate(last_order_id=Max('order__id'))

    # 2. Collections and count of their products
    # queryset = Collection.objects.annotate(count_products=Count('product'))

    # 3. Customers with more than 5 orders
    # queryset = Customer.objects.annotate(
    #     orders_count=Count('order')).filter(orders_count__gt=5)

    # 4. Customers and the total amount they’ve spent
    # queryset = Customer.objects.annotate(total_amount_spent=Sum(
    #     F('order__orderitem__unit_price') * F('order__orderitem__quantity')
    # ))

    # 5. Top 5 best-selling products and their total sales
    queryset = Product.objects.annotate(total_amount_sales=Sum(
        F('orderitem__unit_price') * F('orderitem__quantity')
    )).order_by('-total_amount_sales')[:5]

    return render(request, 'hello.html', {'name': 'Samuel', 'result': list(queryset)})
