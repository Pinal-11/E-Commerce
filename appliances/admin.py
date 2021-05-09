from django.contrib import admin
from .models import wm, air_conditioners, fridge, tv


# Register your models here.

class tv_list(admin.ModelAdmin):
    list_display = ['name', 'price', 'desc', 'image', 'category', 'sub_category', 'color', 'offer']


class wm_list(admin.ModelAdmin):
    list_display = ['name', 'price', 'desc', 'image', 'category', 'sub_category', 'color', 'offer']


class air_conditioners_list(admin.ModelAdmin):
    list_display = ['name', 'price', 'desc', 'image', 'category', 'sub_category', 'color', 'offer']


class fridge_list(admin.ModelAdmin):
    list_display = ['name', 'price', 'desc', 'image', 'category', 'sub_category', 'color', 'offer']


admin.site.register(tv, tv_list),
admin.site.register(wm, wm_list),
admin.site.register(air_conditioners, air_conditioners_list),
admin.site.register(fridge, fridge_list)
