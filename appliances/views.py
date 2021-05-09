from django.shortcuts import render
from .models import tv, wm, fridge, air_conditioners


# Create your views here.

def Television(request):
    t_v = tv.objects.all()
    context = {'query_set_tv': t_v}
    return render(request, 'appliances/Television.html', context)


def category_LED_tv(request):
    t_v = tv.objects.all().filter(screen_type="LED")
    context = {'query_set_tv': t_v}
    return render(request, 'appliances/Television.html', context)


def category_QLED_tv(request):
    t_v = tv.objects.all().filter(screen_type="QLED")
    context = {'query_set_tv': t_v}
    return render(request, 'appliances/Television.html', context)


def category_OLED_tv(request):
    t_v = tv.objects.all().filter(screen_type="OLED")
    context = {'query_set_tv': t_v}
    return render(request, 'appliances/Television.html', context)


def AC(request):
    a_c = air_conditioners.objects.all()
    context = {'query_set_air_conditioners': a_c}
    return render(request, 'appliances/AC.html', context)


def category_inverter_ac(request):
    a_c = air_conditioners.objects.all().filter(Type="inverter AC")
    context = {'query_set_air_conditioners': a_c}
    return render(request, 'appliances/AC.html', context)


def category_window_ac(request):
    a_c = air_conditioners.objects.all().filter(Type="window AC")
    context = {'query_set_air_conditioners': a_c}
    return render(request, 'appliances/AC.html', context)


def category_split_ac(request):
    a_c = air_conditioners.objects.all().filter(Type="Split AC")
    context = {'query_set_air_conditioners': a_c}
    return render(request, 'appliances/AC.html', context)


def category_Coolers(request):
    a_c = air_conditioners.objects.all().filter(category="Cooler")
    context = {'query_set_air_conditioners': a_c}
    return render(request, 'appliances/AC.html', context)


def Refrigerator(request):
    fri = fridge.objects.all()
    context = {'query_set_fridge': fri}
    return render(request, 'appliances/Refrigerator.html', context)


def category_single_door(request):
    fri = fridge.objects.all().filter(Type="single door")
    context = {'query_set_fridge': fri}
    return render(request, 'appliances/Refrigerator.html', context)


def category_double_door(request):
    fri = fridge.objects.all().filter(Type="Double Door")
    context = {'query_set_fridge': fri}
    return render(request, 'appliances/Refrigerator.html', context)


def category_triple_door(request):
    fri = fridge.objects.all().filter(Type="triple door")
    context = {'query_set_fridge': fri}
    return render(request, 'appliances/Refrigerator.html', context)


def category_side_by_side(request):
    fri = fridge.objects.all().filter(Type="side by side")
    context = {'query_set_fridge': fri}
    return render(request, 'appliances/Refrigerator.html', context)


def Washing_machines(request):
    machine = wm.objects.all()
    context = {'query_set_wm': machine}
    return render(request, 'appliances/Washing_machines.html', context)


def category_fully_automatic_front_load(request):
    machine = wm.objects.all().filter(Type="fully automatic front load")
    context = {'query_set_wm': machine}
    return render(request, 'appliances/Washing_machines.html', context)


def category_semi_automatic_top_load(request):
    machine = wm.objects.all().filter(Type="semi automatic top load")
    context = {'query_set_wm': machine}
    return render(request, 'appliances/Washing_machines.html', context)


def category_fully_automatic_top_load(request):
    machine = wm.objects.all().filter(Type="Fully Automatic Top Load")
    context = {'query_set_wm': machine}
    return render(request, 'appliances/Washing_machines.html', context)


def sort_By(request):
    if request.POST.get("tv_price_filter_desc"):
        t_v = tv.objects.all().order_by('-price')
        context = {'query_set_tv': t_v}
        template = "appliances/Television.html"

    if request.POST.get("tv_price_filter_asc"):
        t_v = tv.objects.all().order_by('price')
        context = {'query_set_tv': t_v}
        template = "appliances/Television.html"

    if request.POST.get("tv_special_offer"):
        t_v = tv.objects.all().filter(offer=True)
        context = {'query_set_tv': t_v}
        template = "appliances/Television.html"

    if request.POST.get("ac_price_filter_desc"):
        a_c = air_conditioners.objects.all().order_by('-price')
        context = {'query_set_air_conditioners': a_c}
        template = "appliances/AC.html"

    if request.POST.get("ac_price_filter_asc"):
        a_c = air_conditioners.objects.all().order_by('price')
        context = {'query_set_air_conditioners': a_c}
        template = "appliances/AC.html"

    if request.POST.get("ac_special_offer"):
        a_c = air_conditioners.objects.all().filter(offer=True)
        context = {'query_set_air_conditioners': a_c}
        template = "appliances/AC.html"

    if request.POST.get("fridge_price_filter_desc"):
        fri = fridge.objects.all().order_by('-price')
        context = {'query_set_fridge': fri}
        template = "appliances/Refrigerator.html"

    if request.POST.get("fridge_price_filter_asc"):
        fri = fridge.objects.all().order_by('price')
        context = {'query_set_fridge': fri}
        template = "appliances/Refrigerator.html"

    if request.POST.get("fridge_special_offer"):
        fri = fridge.objects.all().filter(offer=True)
        context = {'query_set_fridge': fri}
        template = "appliances/Refrigerator.html"

    if request.POST.get("wm_price_filter_desc"):
        machine = wm.objects.all().order_by('-price')
        context = {'query_set_wm': machine}
        template = "appliances/Washing_machines.html"

    if request.POST.get("wm_price_filter_asc"):
        machine = wm.objects.all().order_by('price')
        context = {'query_set_wm': machine}
        template = "appliances/Washing_machines.html"

    if request.POST.get("wm_special_offer"):
        machine = wm.objects.all().filter(offer=True)
        context = {'query_set_wm': machine}
        template = "appliances/Washing_machines.html"

    return render(request, template, context)