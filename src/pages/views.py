from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home_view(request,*args, **kwargs): #*args, **kwargs
	return render(request,"home.html",{})
	#HttpResponse("<h1>Hello World</h1>")

def log_view(request,*args, **kwargs): #*args, **kwargs
	return render(request,"log.html",{})
	#HttpResponse("<h1>Hello World</h1>")

def trash_view(request,*args, **kwargs): #*args, **kwargs
	return render(request,"trash.html",{})
	#HttpResponse("<h1>Hello World</h1>")

def test_view(request,*args, **kwargs): 
	context = {
		'boolTest':True,
		'my_text':"THIS IS THE WAY",
		'my_number': 123,
		'my_list':['mal','egd','she','eil'],
	}
	return render(request,"test.html",context)
