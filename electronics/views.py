from django.shortcuts import render
from .models import laptops, cameras, speakers, mobiles


# Create your views here.

def Laptop(request):
    lps = laptops.objects.all()
    context = {'query_set_laptops': lps}
    return render(request, 'electronics/laptops.html', context)


def HP_laptops(request):
    lps = laptops.objects.all().filter(sub_category="HP laptops")
    context = {'query_set_laptops': lps}
    return render(request, 'electronics/laptops.html', context)


def asus_laptops(request):
    lps = laptops.objects.all().filter(sub_category="Asus laptops")
    context = {'query_set_laptops': lps}
    return render(request, 'electronics/laptops.html', context)


def acer_laptops(request):
    lps = laptops.objects.all().filter(sub_category="Acer laptops")
    context = {'query_set_laptops': lps}
    return render(request, 'electronics/laptops.html', context)


def Apple_laptops(request):
    lps = laptops.objects.all().filter(sub_category="Apple laptops")
    context = {'query_set_laptops': lps}
    return render(request, 'electronics/laptops.html', context)


def Mobile(request):
    mob = mobiles.objects.all()
    context = {'query_set_mobiles': mob}
    return render(request, 'electronics/mobiles.html', context)


def Redmi(request):
    mob = mobiles.objects.all().filter(sub_category="Mi mobiles")
    context = {'query_set_mobiles': mob}
    return render(request, 'electronics/mobiles.html', context)


def Realme(request):
    mob = mobiles.objects.all().filter(sub_category="realme mobiles")
    context = {'query_set_mobiles': mob}
    return render(request, 'electronics/mobiles.html', context)


def Samsung(request):
    mob = mobiles.objects.all().filter(sub_category="samsung mobiles")
    context = {'query_set_mobiles': mob}
    return render(request, 'electronics/mobiles.html', context)


def Apple(request):
    mob = mobiles.objects.all().filter(sub_category="apple mobiles")
    context = {'query_set_mobiles': mob}
    return render(request, 'electronics/mobiles.html', context)


def Speaker(request):
    speaks = speakers.objects.all()
    context = {'query_set_speakers': speaks}
    return render(request, 'electronics/speakers.html', context)


def bluetooth_speakers(request):
    speaks = speakers.objects.all().filter(type="bluetooth speaker")
    context = {'query_set_speakers': speaks}
    return render(request, 'electronics/speakers.html', context)


def home_theatres(request):
    speaks = speakers.objects.all().filter(type="home theatre")
    context = {'query_set_speakers': speaks}
    return render(request, 'electronics/speakers.html', context)


def Camera(request):
    cam = cameras.objects.all()
    context = {'query_set_cameras': cam}
    return render(request, 'electronics/cameras.html', context)


def DSLR(request):
    cam = cameras.objects.all().filter(type="DSLR & Mirrorless")
    context = {'query_set_cameras': cam}
    return render(request, 'electronics/cameras.html', context)


def action(request):
    cam = cameras.objects.all().filter(type="action")
    context = {'query_set_cameras': cam}
    return render(request, 'electronics/cameras.html', context)


def sort_By(request):
    if request.POST.get("laptops_price_filter_desc"):
        lps = laptops.objects.all().order_by('-price')
        context = {'query_set_laptops': lps}
        template = "electronics/laptops.html"

    if request.POST.get("laptops_price_filter_asc"):
        lps = laptops.objects.all().order_by('price')
        context = {'query_set_laptops': lps}
        template = "electronics/laptops.html"

    if request.POST.get("laptops_special_offer"):
        lps = laptops.objects.all().filter(offer=True)
        context = {'query_set_laptops': lps}
        template = "electronics/laptops.html"

    if request.POST.get("mobiles_price_filter_desc"):
        mob = mobiles.objects.all().order_by('-price')
        context = {'query_set_mobiles': mob}
        template = "electronics/mobiles.html"

    if request.POST.get("mobiles_price_filter_asc"):
        mob = mobiles.objects.all().order_by('price')
        context = {'query_set_mobiles': mob}
        template = "electronics/mobiles.html"

    if request.POST.get("mobiles_special_offer"):
        mob = mobiles.objects.all().filter(offer=True)
        context = {'query_set_mobiles': mob}
        template = "electronics/mobiles.html"

    if request.POST.get("cameras_price_filter_desc"):
        cam = cameras.objects.all().order_by('-price')
        context = {'query_set_cameras': cam}
        template = "electronics/cameras.html"

    if request.POST.get("cameras_price_filter_asc"):
        cam = cameras.objects.all().order_by('price')
        context = {'query_set_cameras': cam}
        template = "electronics/cameras.html"

    if request.POST.get("cameras_special_offer"):
        cam = cameras.objects.all().filter(offer=True)
        context = {'query_set_cameras': cam}
        template = "electronics/cameras.html"

    if request.POST.get("speakers_price_filter_desc"):
        speaks = speakers.objects.all().order_by('-price')
        context = {'query_set_speakers': speaks}
        template = "electronics/speakers.html"

    if request.POST.get("speakers_price_filter_asc"):
        speaks = speakers.objects.all().order_by('price')
        context = {'query_set_speakers': speaks}
        template = "electronics/speakers.html"

    if request.POST.get("speakers_special_offer"):
        speaks = speakers.objects.all().filter(offer=True)
        context = {'query_set_speakers': speaks}
        template = "electronics/speakers.html"

    return render(request, template, context)
