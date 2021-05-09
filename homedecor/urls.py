from django.urls import path

from . import views

urlpatterns = [
    path('decor', views.decor, name="decor"),
    path('kitchen', views.kitchen, name="kitchen"),
    path('furniture', views.furniture, name="furniture"),

    path('wall_decorations', views.wall_decorations, name="wall_decorations"),
    path('showpieces', views.showpieces, name="showpieces"),

    path('book_shelf', views.book_shelf, name="book_shelf"),
    path('box_beds', views.box_beds, name="box_beds"),

    path('Lunch_box', views.Lunch_box, name="Lunch_box"),
    path('containers', views.containers, name="containers"),
    path('Flasks', views.Flasks, name="Flasks"),
    path('Mixer', views.Mixer, name="Mixer"),
    path('casserole', views.casserole, name="casserole"),

    path('sort_By', views.sort_By, name="sort_By")

]
