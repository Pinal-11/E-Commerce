from django.shortcuts import render
# Create your views here.
from .models import b_cloth, g_cloth, b_footwear, g_footwear


def boys_clothing(request):
    boy = b_cloth.objects.all()
    context = {'query_set_b_cloth': boy}
    return render(request, 'kids/boys_cloth.html', context)


def category_boys_shirts(request):
    boy = b_cloth.objects.all().filter(sub_category="boys shirts")
    context = {'query_set_b_cloth': boy}
    return render(request, 'kids/boys_cloth.html', context)


def category_boys_tshirts(request):
    boy = b_cloth.objects.all().filter(sub_category="boys t-shirts")
    context = {'query_set_b_cloth': boy}
    return render(request, 'kids/boys_cloth.html', context)


def category_boys_ethnic(request):
    boy = b_cloth.objects.all().filter(sub_category="boy's ethnic wear")
    context = {'query_set_b_cloth': boy}
    return render(request, 'kids/boys_cloth.html', context)


def girls_clothing(request):
    girl = g_cloth.objects.all()
    context = {'query_set_g_cloth': girl}
    return render(request, 'kids/girls_cloth.html', context)


def category_girls_tops(request):
    girl = g_cloth.objects.all().filter(sub_category="girls tops")
    context = {'query_set_g_cloth': girl}
    return render(request, 'kids/girls_cloth.html', context)


def category_girls_tshirts(request):
    girl = g_cloth.objects.all().filter(sub_category="girls tshirts")
    context = {'query_set_g_cloth': girl}
    return render(request, 'kids/girls_cloth.html', context)


def category_girls_dresses(request):
    girl = g_cloth.objects.all().filter(sub_category="girls dresses")
    context = {'query_set_g_cloth': girl}
    return render(request, 'kids/girls_cloth.html', context)


def boys_footwear(request):
    boy_f = b_footwear.objects.all()
    context = {'query_set_b_footwear': boy_f}
    return render(request, 'kids/boys_foot.html', context)


def category_boys_sandals(request):
    boy_f = b_footwear.objects.all().filter(sub_category="boys Sandals")
    context = {'query_set_b_footwear': boy_f}
    return render(request, 'kids/boys_foot.html', context)


def category_boys_Sneakers(request):
    boy_f = b_footwear.objects.all().filter(sub_category="boys Sneakers")
    context = {'query_set_b_footwear': boy_f}
    return render(request, 'kids/boys_foot.html', context)


def girls_footwear(request):
    girl_f = g_footwear.objects.all()
    context = {'query_set_g_footwear': girl_f}
    return render(request, 'kids/girls_foot.html', context)


def category_girls_flats(request):
    girl_f = g_footwear.objects.all().filter(sub_category="girls flats")
    context = {'query_set_g_footwear': girl_f}
    return render(request, 'kids/girls_foot.html', context)


def category_girls_sneakers(request):
    girl_f = g_footwear.objects.all().filter(sub_category="girls sneakers")
    context = {'query_set_g_footwear': girl_f}
    return render(request, 'kids/girls_foot.html', context)


def category_girls_casual_shoes(request):
    girl_f = g_footwear.objects.all().filter(sub_category="girls casual shoes")
    context = {'query_set_g_footwear': girl_f}
    return render(request, 'kids/girls_foot.html', context)


def sort_By(request):
    if request.POST.get("girls_cloth_price_filter_desc"):
        girl = g_cloth.objects.all().order_by('-price')
        context = {'query_set_g_cloth': girl}
        template = "kids/girls_cloth.html"

    if request.POST.get("girls_cloth_price_filter_asc"):
        girl = g_cloth.objects.all().order_by('price')
        context = {'query_set_g_cloth': girl}
        template = "kids/girls_cloth.html"

    if request.POST.get("girls_cloth_special_offer"):
        girl = g_cloth.objects.all().filter(offer=True)
        context = {'query_set_g_cloth': girl}
        template = "kids/girls_cloth.html"

    if request.POST.get("boys_cloth_price_filter_desc"):
        boy = b_cloth.objects.all().order_by('-price')
        context = {'query_set_b_cloth': boy}
        template = "kids/boys_cloth.html"

    if request.POST.get("boys_cloth_price_filter_asc"):
        boy = b_cloth.objects.all().order_by('price')
        context = {'query_set_b_cloth': boy}
        template = "kids/boys_cloth.html"

    if request.POST.get("boys_cloth_special_offer"):
        boy = b_cloth.objects.all().filter(offer=True)
        context = {'query_set_b_cloth': boy}
        template = "kids/boys_cloth.html"

    if request.POST.get("boys_foot_price_filter_asc"):
        boy_f = b_footwear.objects.all().order_by('price')
        context = {'query_set_b_footwear': boy_f}
        template = "kids/boys_foot.html"

    if request.POST.get("boys_foot_price_filter_desc"):
        boy_f = b_footwear.objects.all().order_by('-price')
        context = {'query_set_b_footwear': boy_f}
        template = "kids/boys_foot.html"

    if request.POST.get("boys_foot_special_offer"):
        boy_f = b_footwear.objects.all().filter(offer=True)
        context = {'query_set_b_footwear': boy_f}
        template = "kids/boys_foot.html"

    if request.POST.get("girls_footwear_price_filter_asc"):
        girl_f = g_footwear.objects.all().order_by('price')
        context = {'query_set_g_footwear': girl_f}
        template = "kids/girls_foot.html"

    if request.POST.get("girls_footwear_price_filter_desc"):
        girl_f = g_footwear.objects.all().order_by('-price')
        context = {'query_set_g_footwear': girl_f}
        template = "kids/girls_foot.html"

    if request.POST.get("girls_footwear_special_offer"):
        girl_f = g_footwear.objects.all().filter(offer=True)
        context = {'query_set_g_footwear': girl_f}
        template = "kids/girls_foot.html"

    return render(request, template, context)

