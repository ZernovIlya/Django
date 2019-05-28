from configparser import RawConfigParser

from django.core.management.base import BaseCommand
from geekshop.settings import BASE_DIR
from mainapp.models import ProductCategory, Product
from authapp.models import ShopUser


import json, os

local_config_path = os.path.join(BASE_DIR, 'conf', 'local.conf')
config = RawConfigParser()
config.read(local_config_path)



JSON_PATH = 'mainapp/json'

def loadFromJSON(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', encoding='utf-8') as infile:
        return json.load(infile)



class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = loadFromJSON('categories')

        ProductCategory.objects.all().delete()
        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()

        products = loadFromJSON('products')

        Product.objects.all().delete()
        for product in products:
            category_name = product["category"]
            # Получаем категорию по имени
            _category = ProductCategory.objects.get(name=category_name)
            # Заменяем название категории объектом
            product['category'] = _category
            new_product = Product(**product)
            new_product.save()

        # Создаем суперпользователя при помощи менеджера модели
        ShopUser.objects.all().delete()
        ShopUser.objects.create_superuser(config.getboolean('admin', 'ShopUser.objects.create_superuser'))