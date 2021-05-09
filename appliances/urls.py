from django.urls import path

from . import views

urlpatterns = [
    path('television', views.Television, name="television"),
    path('air_conditioners', views.AC, name="air_conditioners"),
    path('refrigerator', views.Refrigerator, name="refrigerator"),
    path('washing_machines', views.Washing_machines, name="wasing_machines"),

    path('inverter_ac', views.category_inverter_ac, name="inverter_ac"),
    path('window_ac', views.category_window_ac, name="window_ac"),
    path('split_ac', views.category_split_ac, name="split_ac"),
    path('Coolers', views.category_Coolers, name="Coolers"),

    path('LED_tv', views.category_LED_tv, name="LED_tv"),
    path('OLED_tv', views.category_OLED_tv, name="OLED_tv"),
    path('QLED_tv', views.category_QLED_tv, name="QLED_tv"),

    path('single_door', views.category_single_door, name="single_door"),
    path('double_door', views.category_double_door, name="double_door"),
    path('triple_door', views.category_triple_door, name="triple_door"),
    path('side_by_side', views.category_side_by_side, name="side_by_side"),

    path('fully_automatic_front_load', views.category_fully_automatic_front_load, name="fully_automatic_front_load"),
    path('semi_automatic_top_load', views.category_semi_automatic_top_load, name="semi_automatic_top_load"),
    path('fully_automatic_top_load', views.category_fully_automatic_top_load, name="fully_automatic_top_load"),

    path('sort_By', views.sort_By, name="sort_By")
]
