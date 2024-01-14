from django.contrib import admin
from .models import Costomer, Basket, OrderProcess
from django.utils.html import format_html

# Register your models here.
class CostomerdAdmin(admin.ModelAdmin):
    list_display = ('username',)
    readonly_fields = ('display_image',)
    search_fields=("username",)

    def display_image(self, obj):
        return format_html('<img src="{}" width="300" height="300" />'.format(obj.image.url))

    display_image.short_description = 'Image'

class OrderAdmin(admin.ModelAdmin):
    list_display=('basket_id','delivered') 
    
    list_filter = (('delivered', admin.BooleanFieldListFilter), )        

admin.site.register(OrderProcess, OrderAdmin)
admin.site.register(Costomer, CostomerdAdmin)
admin.site.register(Basket)
