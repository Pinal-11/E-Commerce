from django.shortcuts import render
from .models import home_furniture, decoration, kitchen_appliance


# Create your views here.

def decor(request):
    dec = decoration.objects.all()
    context = {'query_set_decoration': dec}
    return render(request, 'homedecor/decor.html', context)


def wall_decorations(request):
    dec = decoration.objects.all().filter(sub_category="wall Decorations")
    context = {'query_set_decoration': dec}
    return render(request, 'homedecor/decor.html', context)


def showpieces(request):
    dec = decoration.objects.all().filter(sub_category="showpieces")
    context = {'query_set_decoration': dec}
    return render(request, 'homedecor/decor.html', context)


def kitchen(request):
    kitch = kitchen_appliance.objects.all()
    context = {'query_set_kitchen': kitch}
    return render(request, 'homedecor/kitchen_appliances.html', context)


def Lunch_box(request):
    kitch = kitchen_appliance.objects.all().filter(sub_category="lunch box")
    context = {'query_set_kitchen': kitch}
    return render(request, 'homedecor/kitchen_appliances.html', context)


def containers(request):
    kitch = kitchen_appliance.objects.all().filter(sub_category="container")
    context = {'query_set_kitchen': kitch}
    return render(request, 'homedecor/kitchen_appliances.html', context)


def Flasks(request):
    kitch = kitchen_appliance.objects.all().filter(sub_category="flasks")
    context = {'query_set_kitchen': kitch}
    return render(request, 'homedecor/kitchen_appliances.html', context)


def Mixer(request):
    kitch = kitchen_appliance.objects.all().filter(sub_category="mixer grinder")
    context = {'query_set_kitchen': kitch}
    return render(request, 'homedecor/kitchen_appliances.html', context)


def casserole(request):
    kitch = kitchen_appliance.objects.all().filter(sub_category="casserole")
    context = {'query_set_kitchen': kitch}
    return render(request, 'homedecor/kitchen_appliances.html', context)


def furniture(request):
    furni = home_furniture.objects.all()
    context = {'query_set_home_furniture': furni}
    return render(request, 'homedecor/furniture.html', context)


def book_shelf(request):
    furni = home_furniture.objects.all().filter(sub_category="book shelf")
    context = {'query_set_home_furniture': furni}
    return render(request, 'homedecor/furniture.html', context)


def box_beds(request):
    furni = home_furniture.objects.all().filter(sub_category="Box Beds")
    context = {'query_set_home_furniture': furni}
    return render(request, 'homedecor/furniture.html', context)


def sort_By(request):
    if request.POST.get("decor_price_filter_desc"):
        dec = decoration.objects.all().order_by('-price')
        context = {'query_set_decoration': dec}
        template = "homedecor/decor.html"

    if request.POST.get("decor_price_filter_asc"):
        dec = decoration.objects.all().order_by('price')
        context = {'query_set_decoration': dec}
        template = "homedecor/decor.html"

    if request.POST.get("decor_special_offer"):
        dec = decoration.objects.all().filter(offer=True)
        context = {'query_set_decoration': dec}
        template = "homedecor/decor.html"

    if request.POST.get("fur_price_filter_desc"):
        furni = home_furniture.objects.all().order_by('-price')
        context = {'query_set_home_furniture': furni}
        template = "homedecor/furniture.html"

    if request.POST.get("fur_price_filter_asc"):
        furni = home_furniture.objects.all().order_by('price')
        context = {'query_set_home_furniture': furni}
        template = "homedecor/furniture.html"

    if request.POST.get("fur_special_offer"):
        furni = home_furniture.objects.all().filter(offer=True)
        context = {'query_set_home_furniture': furni}
        template = "homedecor/furniture.html"

    if request.POST.get("ka_price_filter_desc"):
        kitch = kitchen_appliance.objects.all().order_by('-price')
        context = {'query_set_kitchen': kitch}
        template = "homedecor/kitchen_appliances.html"

    if request.POST.get("ka_price_filter_asc"):
        kitch = kitchen_appliance.objects.all().order_by('price')
        context = {'query_set_kitchen': kitch}
        template = "homedecor/kitchen_appliances.html"

    if request.POST.get("ka_special_offer"):
        kitch = kitchen_appliance.objects.all().filter(offer=True)
        context = {'query_set_kitchen': kitch}
        template = "homedecor/kitchen_appliances.html"

    return render(request, template, context)