from django.contrib import admin
from .models import indian_fusion_Wear, western, foot


# Register your models here.

class indian_fusion_Wear_list(admin.ModelAdmin):
    list_display = ['name', 'price', 'desc', 'image', 'category', 'sub_category', 'color', 'offer']


class western_list(admin.ModelAdmin):
    list_display = ['name', 'price', 'desc', 'image', 'category', 'sub_category', 'color', 'offer']


class foot_list(admin.ModelAdmin):
    list_display = ['name', 'price', 'desc', 'image', 'category', 'sub_category', 'color', 'offer']


admin.site.register(indian_fusion_Wear, indian_fusion_Wear_list),
admin.site.register(western, western_list),
admin.site.register(foot, foot_list)
