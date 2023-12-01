from django.contrib import admin
from .models import Category, CharaMake

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

class CharaPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

admin.site.register(Category, CategoryAdmin)
admin.site.register(CharaMake, CharaPostAdmin)