from django.contrib import admin
from .models import b_footwear,b_cloth,g_footwear,g_cloth

# Register your models here.

class b_cloth_list(admin.ModelAdmin):
    list_display = ['name', 'price', 'desc', 'image', 'category', 'sub_category', 'color', 'offer']

class b_footwear_list(admin.ModelAdmin):
    list_display = ['name', 'price', 'desc', 'image', 'category', 'sub_category', 'color', 'offer']

class g_cloth_list(admin.ModelAdmin):
    list_display = ['name', 'price', 'desc', 'image', 'category', 'sub_category', 'color', 'offer']

class g_footwear_list(admin.ModelAdmin):
    list_display = ['name', 'price', 'desc', 'image', 'category', 'sub_category', 'color', 'offer']

admin.site.register(b_cloth, b_cloth_list),
admin.site.register(b_footwear, b_footwear_list),
admin.site.register(g_footwear,g_footwear_list),
admin.site.register(g_cloth, g_cloth_list)