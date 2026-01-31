from django.shortcuts import render

# Create your views here.


def accueil(request):
    return render(request, 'index.html')



# Vue pour la page Projets
def projets(request):
    return render(request, "projets.html")

# Vue pour la page Compétences
def competences(request):
    return render(request, "competences.html")


# Vue pour la page Contact
def contact(request):
    return render(request, "contact.html")
