from django.shortcuts import render
from .models import mens_indian_Wear, footwear, topwear


# Create your views here.

def mens_indian_wear(request):
    mens = mens_indian_Wear.objects.all()
    context = {'query_set_mens_indian_Wear': mens}
    return render(request, 'mens/mens_indian_wear.html', context)


def category_waistcoats(request):
    mens = mens_indian_Wear.objects.all().filter(sub_category="men's waistcoats")
    context = {'query_set_mens_indian_Wear': mens}
    return render(request, 'mens/mens_indian_wear.html', context)


def category_kurtas(request):
    mens = mens_indian_Wear.objects.all().filter(sub_category="men's kurtas")
    context = {'query_set_mens_indian_Wear': mens}
    return render(request, 'mens/mens_indian_wear.html', context)


def category_sherwanis(request):
    mens = mens_indian_Wear.objects.all().filter(sub_category="men's sherwanis")
    context = {'query_set_mens_indian_Wear': mens}
    return render(request, 'mens/mens_indian_wear.html', context)


def mens_topwear(request):
    top = topwear.objects.all()
    context = {'query_set_topwear': top}
    return render(request, 'mens/mens_topwear.html', context)


def category_mens_blazer(request):
    top = topwear.objects.all().filter(sub_category="men's blazers")
    context = {'query_set_topwear': top}
    return render(request, 'mens/mens_topwear.html', context)


def category_mens_shirts(request):
    top = topwear.objects.all().filter(sub_category="men's shirts")
    context = {'query_set_topwear': top}
    return render(request, 'mens/mens_topwear.html', context)


def category_mens_tshirts(request):
    top = topwear.objects.all().filter(sub_category="men's t-shirts")
    context = {'query_set_topwear': top}
    return render(request, 'mens/mens_topwear.html', context)


def mens_footwear(request):
    foot = footwear.objects.all()
    context = {'query_set_footwear': foot}
    return render(request, 'mens/mens_footwear.html', context)


def category_mens_casual_shoes(request):
    foot = footwear.objects.all().filter(sub_category="Casual shoes")
    context = {'query_set_footwear': foot}
    return render(request, 'mens/mens_footwear.html', context)


def category_mens_formal_shoes(request):
    foot = footwear.objects.all().filter(sub_category="formal shoes")
    context = {'query_set_footwear': foot}
    return render(request, 'mens/mens_footwear.html', context)


def category_mens_sports_shoes(request):
    foot = footwear.objects.all().filter(sub_category="sports shoes")
    context = {'query_set_footwear': foot}
    return render(request, 'mens/mens_footwear.html', context)


def category_mens_sneakers(request):
    foot = footwear.objects.all().filter(sub_category="Sneakers")
    context = {'query_set_footwear': foot}
    return render(request, 'mens/mens_footwear.html', context)


def category_mens_floaters(request):
    foot = footwear.objects.all().filter(sub_category="floaters")
    context = {'query_set_footwear': foot}
    return render(request, 'mens/mens_footwear.html', context)


def sort_By(request):
    if request.POST.get("mens_footwear_price_filter_desc"):
        foot = footwear.objects.all().order_by('-price')
        context = {'query_set_footwear': foot}
        template = "mens/mens_footwear.html"

    if request.POST.get("mens_footwear_price_filter_asc"):
        foot = footwear.objects.all().order_by('price')
        context = {'query_set_footwear': foot}
        template = "mens/mens_footwear.html"

    if request.POST.get("mens_footwear_special_offer"):
        foot = footwear.objects.all().filter(offer=True)
        context = {'query_set_footwear': foot}
        template = "mens/mens_footwear.html"

    if request.POST.get("mens_indian_wear_price_filter_desc"):
        mens = mens_indian_Wear.objects.all().order_by('-price')
        context = {'query_set_mens_indian_Wear': mens}
        template = "mens/mens_indian_wear.html"

    if request.POST.get("mens_indian_wear_price_filter_asc"):
        mens = mens_indian_Wear.objects.all().order_by('price')
        context = {'query_set_mens_indian_Wear': mens}
        template = "mens/mens_indian_wear.html"

    if request.POST.get("mens_indian_wear_special_offer"):
        mens = mens_indian_Wear.objects.all().filter(offer=True)
        context = {'query_set_mens_indian_Wear': mens}
        template = "mens/mens_indian_wear.html"

    if request.POST.get("mens_topwear_price_filter_desc"):
        top = topwear.objects.all().order_by('-price')
        context = {'query_set_topwear': top}
        template = "mens/mens_topwear.html"

    if request.POST.get("mens_topwear_price_filter_asc"):
        top = topwear.objects.all().order_by('price')
        context = {'query_set_topwear': top}
        template = "mens/mens_topwear.html"

    if request.POST.get("mens_topwear_special_offer"):
        top = topwear.objects.all().filter(offer=True)
        context = {'query_set_topwear': top}
        template = "mens/mens_topwear.html"

    return render(request, template, context)
