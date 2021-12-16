from django.shortcuts import render
import json
# Create your views here.


with open('mainapp/main_menu.json', 'r', encoding='utf-8') as menu_file:
    main_menu_links_dict = json.load(menu_file)
main_menu_links = [i for i in main_menu_links_dict['menu_links']]

with open('mainapp/prod_menu.json', 'r', encoding='utf-8') as prod_menu:
    prods_menu = json.load(prod_menu)


def index(request):

    return render(request, 'mainapp/index.html', context={'main_menu_links': main_menu_links})


def products(request):
    prod_menu_links = [i for i in prods_menu['prod_menu']]
    return render(request, 'mainapp/products.html', context={'main_menu_links': main_menu_links,
                                                             'prod_menu_links': prod_menu_links})


def contact(request):
    return render(request, 'mainapp/contact.html', context={'main_menu_links': main_menu_links})