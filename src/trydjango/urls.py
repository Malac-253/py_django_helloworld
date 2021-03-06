"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#my views
from pages.views import home_view, log_view, trash_view, test_view
from products.views import product_detail_view, product_create_view

urlpatterns = [
    path('admin/', admin.site.urls),

    #My views
    path('',home_view, name='Home'),
    path('home/',home_view, name='Home'),
    path('test/',test_view, name='Testing Page'),
    path('log/',log_view, name='LOG'),
    path('trash/',trash_view, name='POOPY FACE'),

    path('product/',product_detail_view, name='Details'),
    path('create/',product_create_view, name='Create'),

]
