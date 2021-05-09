from django.contrib import admin
from .models import cameras, laptops, mobiles, speakers


# Register your models here.

class cameras_list(admin.ModelAdmin):
    list_display = ['name', 'price', 'desc', 'image', 'category', 'sub_category', 'color', 'offer']


class laptops_list(admin.ModelAdmin):
    list_display = ['name', 'price', 'desc', 'image', 'category', 'sub_category', 'color', 'offer']


class mobiles_list(admin.ModelAdmin):
    list_display = ['name', 'price', 'desc', 'image', 'category', 'sub_category', 'color', 'offer']


class speakers_list(admin.ModelAdmin):
    list_display = ['name', 'price', 'desc', 'image', 'category', 'sub_category', 'color', 'offer']


admin.site.register(cameras, cameras_list),
admin.site.register(laptops, laptops_list),
admin.site.register(mobiles, mobiles_list),
admin.site.register(speakers, speakers_list)
