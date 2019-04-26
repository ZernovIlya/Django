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
