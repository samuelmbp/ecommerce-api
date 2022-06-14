from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product

# NOTE: Every models class has a manager 'objects'


def say_hello(request):
    exists = Product.objects.filter(pk=0).exists()

    return render(request, 'hello.html', {'name': 'Samuel'})
