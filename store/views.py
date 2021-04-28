from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def categories(request):
	categories_list = Category.objects.all()
	return {'categories': categories_list}


def all_products(request):
	products = Product.objects.all()
	return render(request, 'store/home.html', {'products': products})


def product_detail(request, slug):
	product = get_object_or_404(Product, slug=slug, in_stock=True)
	return render(request, 'store/home.html', {'product': product})
