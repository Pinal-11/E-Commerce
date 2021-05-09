from django.shortcuts import render, redirect
from django.db.models import Q
from appliances.models import *
from electronics.models import *
from homedecor.models import *
from kids.models import *
from mens.models import *
from womens.models import *

# Create your views here.


def home(request):
    print(request.session.get('name'))
    return render(request, 'homepage.html')


def about(request):
    return render(request, 'about.html')


def search(request):
    try:
        q = request.GET.get("query")
    except:
        q = None

    if q:
        query_set_b_cloth = b_cloth.objects.all().filter(Q(category__iexact=q) | Q(sub_category__iexact=q))
        query_set_g_cloth = g_cloth.objects.all().filter(Q(category__iexact=q) | Q(sub_category__iexact=q))
        query_set_b_footwear = b_footwear.objects.all().filter(Q(category__iexact=q) | Q(sub_category__iexact=q))
        query_set_g_footwear = g_footwear.objects.all().filter(Q(category__iexact=q) | Q(sub_category__iexact=q))

        query_set_tv = tv.objects.all().filter(Q(category__iexact=q) | Q(sub_category__iexact=q))
        query_set_wm = wm.objects.all().filter(Q(category__iexact=q) | Q(sub_category__iexact=q))
        query_set_fridge = fridge.objects.all().filter(Q(category__iexact=q) | Q(sub_category__iexact=q))
        query_set_air_conditioners = air_conditioners.objects.all().filter(
            Q(category__iexact=q) | Q(sub_category__iexact=q))

        query_set_laptops = laptops.objects.all().filter(Q(category__iexact=q) | Q(sub_category__iexact=q))
        query_set_mobiles = mobiles.objects.all().filter(Q(category__iexact=q) | Q(sub_category__iexact=q))
        query_set_speakers = speakers.objects.all().filter(Q(category__iexact=q) | Q(sub_category__iexact=q))
        query_set_cameras = cameras.objects.all().filter(Q(category__iexact=q) | Q(sub_category__iexact=q))

        query_set_home_furniture = home_furniture.objects.all().filter(
            Q(category__iexact=q) | Q(sub_category__iexact=q))
        query_set_decoration = decoration.objects.all().filter(Q(category__iexact=q) | Q(sub_category__iexact=q))
        query_set_kitchen = kitchen_appliance.objects.all().filter(Q(category__iexact=q) | Q(sub_category__iexact=q))

        query_set_mens_indian_Wear = mens_indian_Wear.objects.all().filter(
            Q(category__iexact=q) | Q(sub_category__iexact=q))
        query_set_footwear = footwear.objects.all().filter(Q(category__iexact=q) | Q(sub_category__iexact=q))
        query_set_topwear = topwear.objects.all().filter(Q(category__iexact=q) | Q(sub_category__iexact=q))

        query_set_western = western.objects.all().filter(Q(category__iexact=q) | Q(sub_category__iexact=q))
        query_set_indian_fusion_Wear = indian_fusion_Wear.objects.all().filter(
            Q(category__iexact=q) | Q(sub_category__iexact=q))
        query_set_foot = foot.objects.all().filter(Q(category__iexact=q) | Q(sub_category__iexact=q))

        context = {'query_set_b_cloth': query_set_b_cloth, 'query_set_g_cloth': query_set_g_cloth,
                   'query_set_b_footwear': query_set_b_footwear, 'query_set_g_footwear': query_set_g_footwear,

                   'query_set_tv': query_set_tv, 'query_set_wm': query_set_wm, 'query_set_fridge': query_set_fridge,
                   'query_set_air_conditioners': query_set_air_conditioners, 'query_set_laptops': query_set_laptops,
                   'query_set_mobiles': query_set_mobiles, 'query_set_speakers': query_set_speakers,
                   'query_set_cameras': query_set_cameras, 'query_set_home_furniture': query_set_home_furniture,
                   'query_set_decoration': query_set_decoration, 'query_set_kitchen': query_set_kitchen,
                   'query_set_mens_indian_Wear': query_set_mens_indian_Wear, 'query_set_topwear': query_set_topwear,
                   'query_set_footwear': query_set_footwear, 'query_set_western': query_set_western,
                   'query_set_indian_fusion_Wear': query_set_indian_fusion_Wear, 'query_set_foot': query_set_foot
                   }

        if query_set_b_cloth:
            template = 'kids/boys_cloth.html'
        elif query_set_g_cloth:
            template = 'kids/girls_cloth.html'
        elif query_set_b_footwear:
            template = 'kids/boys_foot.html'
        elif query_set_g_footwear:
            template = 'kids/girls_foot.html'
        elif query_set_home_furniture:
            template = 'homedecor/furniture.html'
        elif query_set_decoration:
            template = 'homedecor/decor.html'
        elif query_set_kitchen:
            template = 'homedecor/kitchen_appliances.html'
        elif query_set_tv:
            template = 'appliances/Television.html'
        elif query_set_wm:
            template = 'appliances/Washing_machines.html'
        elif query_set_fridge:
            template = 'appliances/Refrigerator.html'
        elif query_set_air_conditioners:
            template = 'appliances/AC.html'
        elif query_set_laptops:
            template = 'electronics/laptops.html'
        elif query_set_cameras:
            template = 'electronics/cameras.html'
        elif query_set_speakers:
            template = 'electronics/speakers.html'
        elif query_set_mobiles:
            template = 'electronics/mobiles.html'
        elif query_set_mens_indian_Wear:
            template = 'mens/mens_indian_wear.html'
        elif query_set_topwear:
            template = 'mens/mens_topwear.html'
        elif query_set_footwear:
            template = 'mens/mens_footwear.html'
        elif query_set_foot:
            template = 'womens/womens_footwear.html'
        elif query_set_western:
            template = 'womens/western_wear.html'
        elif query_set_indian_fusion_Wear:
            template = 'womens/indian_wear.html'

        return render(request, template, context)

    else:
        template = 'homepage.html'
        return redirect(request, template)
