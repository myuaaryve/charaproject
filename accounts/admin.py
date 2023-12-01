from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_dispray = ('id', 'username')
    list_dispray_links = ('id', 'username')

admin.site.register(CustomUser, CustomUserAdmin)
