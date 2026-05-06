from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInLine(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInLine]
    list_display = ('id', 'first_name', 'last_name', 'email', 'created_at')
    list_filter = ('first_name', 'created_at')
    search_fields = ('first_name', 'last_name', 'email')

    def get_total_cost(self):
        return sum(item.total_price() for item in self.items.all())


    get_total_cost.short_description = 'Total Cost'
