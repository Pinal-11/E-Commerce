from django.urls import path

from . import views

urlpatterns = [
    path('indian_festive_wear',views.mens_indian_wear,name="mens_indian_wear"),
    path('topwear',views.mens_topwear,name="mens_topwear"),
    path('footwear',views.mens_footwear,name="mens_footwear"),

    path("kurtas",views.category_kurtas,name="category_kurtas"),
    path("sherwanis",views.category_sherwanis,name="category_sherwanis"),
    path("waistcoats",views.category_waistcoats,name="category_waistcoats"),

    path("mens_shirts",views.category_mens_shirts,name="category_mens_shirts"),
    path("mens_tshirts",views.category_mens_tshirts,name="category_mens_tshirts"),
    path("mens_blazer",views.category_mens_blazer,name="category_mens_blazer"),

    path('mens_casual_shoes',views.category_mens_casual_shoes,name="mens_casual_shoes"),
    path('mens_formal_shoes',views.category_mens_formal_shoes,name="mens_formal_shoes"),
    path('mens_sports_shoes',views.category_mens_sports_shoes,name="mens_sports_shoes"),
    path('mens_sneakers',views.category_mens_sneakers,name="mens_sneakers"),
    path('mens_floaters',views.category_mens_floaters,name="mens_floaters"),
    path('sort_By',views.sort_By,name="sort_By")
]