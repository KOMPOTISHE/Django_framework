from django.shortcuts import render
from datetime import datetime

def index(request):
    menu_links = [
        {'view_name': 'index', 'name': 'домой'},
        {'view_name': 'products', 'name': 'продукты'},
        {'view_name': 'contact', 'name': 'контакт'},
    ]
    return render(request, 'mainapp/index.html', context={'menu_links': menu_links})

    


def contact(request):
    menu_links = [
        {'view_name': 'index', 'name': 'домой'},
        {'view_name': 'products', 'name': 'продукты'},
        {'view_name': 'contact', 'name': 'контакт'},
    ]
    return render(request, 'mainapp/contact.html', context={'menu_links': menu_links})


def products(request):
    menu_links = [
        {'view_name': 'index', 'name': 'домой'},
        {'view_name': 'products', 'name': 'продукты'},
        {'view_name': 'contact', 'name': 'контакт'},
    ]
    return render(request, 'mainapp/products.html', context={'menu_links': menu_links})