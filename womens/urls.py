from django.urls import path

from . import views

urlpatterns = [
    path('indian_wear', views.indian_wear, name="indian_wear"),
    path('western_wear', views.western_wear, name="western_wear"),
    path('womens_footwear', views.foot_wear, name="foot_wear"),

    path('sarees', views.category_sarees, name="sarees"),
    path('Ethnic_dresses', views.category_Ethnic_dresses, name="Ethnic_dresses"),
    path('Kurtas', views.category_Kurtas, name="Kurtas"),

    path('dresses_jumpsuits', views.category_dresses, name="dresses_jumpsuits"),
    path('tops_tshirts_shirts', views.category_tops_tshirts_shirts, name="tops_tshirts_shirts"),
    path('shrugs_jackets', views.category_shrugs, name="shrugs_jackets"),

    path('Flats', views.category_Flats, name="Flats"),
    path('Heels', views.category_Heels, name="Heels"),
    path('Sandals', views.category_Sandals, name="Sandals"),
    path('mojaris', views.category_mojaris, name="mojaris"),
    path('Casual_Shoes', views.category_Casual_Shoes, name="Casual_Shoes"),
    path('sort_By', views.sort_By, name="sort_By")
]
