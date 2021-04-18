from django.shortcuts import render
from .models import Category, Product


def categories(request):
	categories_list = Category.objects.all()
	return {'categories': categories_list}


def all_products(request):
	products = Product.objects.all()
	return render(request, 'store/home.html', {'products': products})
