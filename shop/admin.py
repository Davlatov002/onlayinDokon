from django.contrib import admin
from .models import Praduct, Category
from django.utils.html import format_html

class PraductdAdmin(admin.ModelAdmin):
    list_display = ('name','existence')
    list_filter = (('existence', admin.BooleanFieldListFilter), )
    readonly_fields = ('display_praduct_image',)
    search_fields=("name",)

    def display_praduct_image(self, obj):
        return format_html('<img src="{}" width="300" height="300" />'.format(obj.praduct_image.url))

    display_praduct_image.short_description = 'Praduct Image'
    


admin.site.register(Praduct, PraductdAdmin)
admin.site.register(Category)


