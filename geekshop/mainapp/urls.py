from django.conf.urls import url
from django.urls import path
import mainapp.views as mainapp

from mainapp.views import products

app_name = 'mainapp'

urlpatterns = [
    path('', products, name='index'),
    url(r'^category/(?P<pk>\d+)/$', mainapp.products, name='category')
]