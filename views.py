from django.shortcuts import render, get_object_or_404
from .models import Style, Malt, MaltWeight, HopAcid, Hop, HopAddition, Yeast, Recipe

def hops(request):
    hops = Hop.objects.all().order_by('name', '-alpha_acid')
    context = {'hops': hops }
    return render(request, 'brew/hops.html', context)

def hop(request, hop):
    hop = get_object_or_404(Hop, slug = hop)
    context = {'hop': hop }
    return render(request, 'brew/hop.html', context)

def malts(request):
    malts = Malt.objects.all().order_by('name', 'lovibond')
    context = {'malts': malts }
    return render(request, 'brew/malts.html', context)

def malt(request, malt):
    malt = get_object_or_404(Malt, slug = malt)
    context = {'malt': malt }
    return render(request, 'brew/malt.html', context)

def styles(request):
    styles = Style.objects.all().order_by('name')
    context = {'styles': styles }
    return render(request, 'brew/styles.html', context)

def style(request, style):
    style = get_object_or_404(Style, slug = style)
    context = {'style': style }
    return render(request, 'brew/style.html', context)