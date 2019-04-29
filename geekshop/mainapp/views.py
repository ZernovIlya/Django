from django.shortcuts import render


def main(request):
    context = {'user':{'name':'человек'}}
    return render(request, 'mainapp/index.html', context)


def products(request):
    return render(request, 'mainapp/helicopter.html')


def contact(request):
    return render(request, 'mainapp/contacts.html')


from django.shortcuts import render

# Create your views here.
from .models import ProductCategory, Product
def main (request):
    title = 'главная'
    products = Product.objects.all()[: 4 ]
    content = { 'title' : title, 'products' : products}
    return render(request, 'mainapp/index.html' , content)