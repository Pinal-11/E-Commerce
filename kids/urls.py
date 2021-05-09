from django.urls import path

from . import views

urlpatterns = [
    path('boys_clothing', views.boys_clothing, name="boys_clothing"),
    path('girls_clothing', views.girls_clothing, name="girls_clothing"),
    path('boys_footwear', views.boys_footwear, name="boys_footwear"),
    path('girls_footwear', views.girls_footwear, name="girls_footwear"),

    path('boys_shirts', views.category_boys_shirts, name="boys_shirts"),
    path('boys_tshirts', views.category_boys_tshirts, name="boys_tshirts"),
    path('boys_ethnic', views.category_boys_ethnic, name="boys_ethnic"),

    path('girls_tops', views.category_girls_tops, name="girls_tops"),
    path('girls_tshirts', views.category_girls_tshirts, name="girls_tshirts"),
    path('girls_dresses', views.category_girls_dresses, name="girls_dresses"),

    path('boys_Sneakers', views.category_boys_Sneakers, name="boys_Sneakers"),
    path('boys_sandals', views.category_boys_sandals, name="boys_sandals"),

    path('girls_flats', views.category_girls_flats, name="girls_flats"),
    path('girls_sneakers', views.category_girls_sneakers, name="girls_sneakers"),
    path('girls_casual_shoes', views.category_girls_casual_shoes, name="girls_casual_shoes"),

    path('sort_By', views.sort_By, name="sort_By")
]
