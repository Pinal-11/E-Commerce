from django.contrib import admin
from .models import home_furniture, decoration, kitchen_appliance


# Register your models here.

class home_furniture_list(admin.ModelAdmin):
    list_display = ['name', 'price', 'desc', 'image', 'category', 'sub_category', 'color', 'offer']


class decoration_list(admin.ModelAdmin):
    list_display = ['name', 'price', 'desc', 'image', 'category', 'sub_category', 'color', 'offer']


class kitchen_appliance_list(admin.ModelAdmin):
    list_display = ['name', 'price', 'desc', 'image', 'category', 'sub_category', 'color', 'offer']


admin.site.register(home_furniture, home_furniture_list),
admin.site.register(decoration, decoration_list),
admin.site.register(kitchen_appliance, kitchen_appliance_list)
