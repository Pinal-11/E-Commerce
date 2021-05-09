from django.contrib import admin
from .models import mens_indian_Wear, topwear, footwear


# Register your models here.

class mens_indian_Wear_list(admin.ModelAdmin):
    list_display = ['name', 'price', 'desc', 'image', 'category', 'sub_category', 'color', 'offer']


class topwear_list(admin.ModelAdmin):
    list_display = ['name', 'price', 'desc', 'image', 'category', 'sub_category', 'color', 'offer']


class footwear_list(admin.ModelAdmin):
    list_display = ['name', 'price', 'desc', 'image', 'category', 'sub_category', 'color', 'offer']


admin.site.register(mens_indian_Wear, mens_indian_Wear_list),
admin.site.register(topwear, topwear_list),
admin.site.register(footwear, footwear_list)
