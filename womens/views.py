from django.shortcuts import render
from .models import indian_fusion_Wear, western, foot


# Create your views here.

def indian_wear(request):
    indian = indian_fusion_Wear.objects.all()
    context = {'query_set_indian_fusion_Wear': indian}
    return render(request, 'womens/indian_wear.html', context)


def category_sarees(request):
    indian = indian_fusion_Wear.objects.all().filter(sub_category="sarees")
    context = {'query_set_indian_fusion_Wear': indian}
    return render(request, 'womens/indian_wear.html', context)


def category_Ethnic_dresses(request):
    indian = indian_fusion_Wear.objects.all().filter(sub_category="lehengas")
    context = {'query_set_indian_fusion_Wear': indian}
    return render(request, 'womens/indian_wear.html', context)


def category_Kurtas(request):
    indian = indian_fusion_Wear.objects.all().filter(sub_category="kurtaset")
    context = {'query_set_indian_fusion_Wear': indian}
    return render(request, 'womens/indian_wear.html', context)


def western_wear(request):
    west = western.objects.all()
    context = {'query_set_western': west}
    return render(request, 'womens/western_wear.html', context)


def category_dresses(request):
    west = western.objects.all().filter(sub_category="dresses & Jumpsuits")
    context = {'query_set_western': west}
    return render(request, 'womens/western_wear.html', context)


def category_tops_tshirts_shirts(request):
    west = western.objects.all().filter(sub_category="women's tops")
    context = {'query_set_western': west}
    return render(request, 'womens/western_wear.html', context)


def category_shrugs(request):
    west = western.objects.all().filter(sub_category="women's shrugs")
    context = {'query_set_western': west}
    return render(request, 'womens/western_wear.html', context)


def foot_wear(request):
    w_f = foot.objects.all()
    context = {'query_set_foot': w_f}
    return render(request, 'womens/womens_footwear.html', context)


def category_Flats(request):
    w_f = foot.objects.all().filter(sub_category="flats")
    context = {'query_set_foot': w_f}
    return render(request, 'womens/womens_footwear.html', context)


def category_Heels(request):
    w_f = foot.objects.all().filter(sub_category="heels")
    context = {'query_set_foot': w_f}
    return render(request, 'womens/womens_footwear.html', context)


def category_Sandals(request):
    w_f = foot.objects.all().filter(sub_category="women's sandals")
    context = {'query_set_foot': w_f}
    return render(request, 'womens/womens_footwear.html', context)


def category_Casual_Shoes(request):
    w_f = foot.objects.all().filter(sub_category="women's sneakers")
    context = {'query_set_foot': w_f}
    return render(request, 'womens/womens_footwear.html', context)


def category_mojaris(request):
    w_f = foot.objects.all().filter(sub_category="mojaris")
    context = {'query_set_foot': w_f}
    return render(request, 'womens/womens_footwear.html', context)


def sort_By(request):
    if request.POST.get("western_price_filter_desc"):
        west = western.objects.all().order_by('-price')
        context = {'query_set_western': west}
        template = "womens/western_wear.html"

    if request.POST.get("western_price_filter_asc"):
        west = western.objects.all().order_by('price')
        context = {'query_set_western': west}
        template = "womens/western_wear.html"

    if request.POST.get("western_special_offer"):
        west = western.objects.all().filter(offer=True)
        context = {'query_set_western': west}
        template = "womens/western_wear.html"

    if request.POST.get("womens_footwear_price_filter_desc"):
        w_f = foot.objects.all().order_by('-price')
        context = {'query_set_foot': w_f}
        template = "womens/womens_footwear.html"

    if request.POST.get("womens_footwear_price_filter_asc"):
        w_f = foot.objects.all().order_by('price')
        context = {'query_set_foot': w_f}
        template = "womens/womens_footwear.html"

    if request.POST.get("womens_footwear_special_offer"):
        w_f = foot.objects.all().filter(offer=True)
        context = {'query_set_foot': w_f}
        template = "womens/womens_footwear.html"

    if request.POST.get("womens_indian_wear_price_filter_desc"):
        indian = indian_fusion_Wear.objects.all().order_by('-price')
        context = {'query_set_indian_fusion_Wear': indian}
        template = "womens/indian_wear.html"

    if request.POST.get("womens_indian_wear_price_filter_asc"):
        indian = indian_fusion_Wear.objects.all().order_by('price')
        context = {'query_set_indian_fusion_Wear': indian}
        template = "womens/indian_wear.html"

    if request.POST.get("womens_indian_wear_special_offer"):
        indian = indian_fusion_Wear.objects.all().filter(offer=True)
        context = {'query_set_indian_fusion_Wear': indian}
        template = "womens/indian_wear.html"

    return render(request, template, context)

