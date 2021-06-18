from django.shortcuts import render

# Create your views here.
from .models import Product


def product_detail_view(request):
	obj = Product.objects.get(id=1)
		# context = {
		# 	'title':obj.title,
		# 	'description': obj.description,
		# 	'price': obj.price,
		# 	'summary': obj.summary,
		# 	'featured': obj.featured,
		# }
	context = {'obj':obj}
 
	return render(request ,"products/detail.html",context)

from .forms import ProductForm

# the simplest easy way
# def product_create_view(request):
# 	form = ProductForm(request.POST or None)

# 	if form.is_valid():
# 		form.save()
# 		form = ProductForm()

# 	context = {'form':form}
 
# 	return render(request ,"products/product_create.html",context)

# the simplest easy way
def product_create_view(request):
	print(request.GET)
	print(request.POST)
	
	context = {}
	return render(request ,"products/product_create.html",context)