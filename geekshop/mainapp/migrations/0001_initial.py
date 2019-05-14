# Generated by Django 2.2 on 2019-05-13 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='имя категории')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание категории')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='имя продукта')),
                ('image', models.ImageField(blank=True, upload_to='products_images')),
                ('short_desc', models.CharField(blank=True, max_length=60, null=True, verbose_name='кратко')),
                ('description', models.TextField(blank=True, verbose_name='подробно')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='цена')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='склад')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.ProductCategory', verbose_name='категория товара')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
            },
        ),
    ]
