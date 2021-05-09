from django.urls import path

from . import views

urlpatterns = [
    path('laptops', views.Laptop, name="laptops"),
    path('mobiles', views.Mobile, name="mobiles"),
    path('speakers', views.Speaker, name="speakers"),
    path('cameras', views.Camera, name="cameras"),

    path('DSLR', views.DSLR, name="DSLR"),
    path('action', views.action, name="action"),

    path('HP_laptops', views.HP_laptops, name="HP_laptops"),
    path('acer_laptops', views.acer_laptops, name="acer_laptops"),
    path('Apple_laptops', views.Apple_laptops, name="Apple_laptops"),
    path('asus_laptops', views.asus_laptops, name="asus_laptops"),

    path('Redmi', views.Redmi, name="Redmi"),
    path('Realme', views.Realme, name="Realme"),
    path('Samsung', views.Samsung, name="Samsung"),
    path('Apple', views.Apple, name="Apple"),

    path('bluetooth_speakers', views.bluetooth_speakers, name="bluetooth_speakers"),
    path('home_theatres', views.home_theatres, name="home_theatres"),

    path('sort_By', views.sort_By, name="sort_By")
]
