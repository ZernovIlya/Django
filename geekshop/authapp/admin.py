from django.contrib import admin
from .models import ShopUser
from basketapp.models import BasketSlot


admin.site.register(ShopUser)

class BasketInline(admin.TabularInline):
    model = BasketSlot
    fields = 'product', 'quantity'
    extra = 0


class UsersWithBasket(ShopUser):
    class Meta:
        verbose_name = 'Пользователь с корзиной'
        verbose_name_plural = 'Пользователи с корзиной'
        proxy = True


@admin.register(UsersWithBasket)
class UsersWithBasketAdmin(admin.ModelAdmin):
    list_display = 'username', 'get_basket_qiantity', 'get_basket_cost'
    fields = 'username',
    readonly_fields = 'username',
    inlines = BasketInline,

    def get_queryset(self, request):
        qs = super(UsersWithBasketAdmin, self).get_queryset(request)
        return qs.filter(basket__quantity__gt=0).distinct()

    def get_basket_qiantity(self, instance):
        basket = BasketSlot.objects.filter(user=instance)
        return sum(list(map(lambda basket_slot: basket_slot.quantity, basket)))

    get_basket_qiantity.short_description = 'Товаров в корзине'

    def get_basket_cost(self, instance):
        basket = BasketSlot.objects.filter(user=instance)
        return sum(list(map(lambda x: x.product.price * x.quantity, basket)))

    get_basket_cost.short_description = 'Общая стоимость корзины'