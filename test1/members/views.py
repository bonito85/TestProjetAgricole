from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Member, Cooperative

def index(request):
    template = loader.get_template('index.html')
    return render(request, 'index.html')



def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('liste_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def liste_cooperative(request):
    coop = Cooperative.objects.all().values()
    template = loader.get_template('liste_cooperative.html')
    context = {
        'coop': coop,
    }
    # Retourner la réponse avec le rendu du template et le contexte
    return render(request, 'liste_cooperative.html', context)


def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
    'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

"""def details_coop(request, id):
    coop_details = Member.objects.get(id=id)
    template = loader.get_template('details_coop.html')
    context = {
    'coop_details': coop_details,
    }
    return HttpResponse(template.render(context, request))"""

def details_coop(request, id):
    # Récupérer l'objet Cooperative correspondant à l'id
    coop_details = get_object_or_404(Cooperative, id=id)

    # Contexte pour passer les détails de la coopérative au template
    context = {
        'coop_details': coop_details,
    }

    # Utilisez render pour simplifier le rendu du template
    return render(request, 'details_coop.html', context)
