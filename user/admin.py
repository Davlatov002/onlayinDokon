from django.contrib import admin
from .models import Costomer, Basket
from django.utils.html import format_html

# Register your models here.
class CostomerdAdmin(admin.ModelAdmin):
    list_display = ('username',)
    readonly_fields = ('display_image',)
    search_fields=("username",)

    def display_image(self, obj):
        return format_html('<img src="{}" width="300" height="300" />'.format(obj.image.url))

    display_image.short_description = 'Image'
         

admin.site.register(Costomer, CostomerdAdmin)
admin.site.register(Basket)
