from django.shortcuts import render, redirect
from django.contrib import messages

import os
from dashadmin.models import Article, CategorieArticle, Projet, Album, Galerie, Ressource, Benevole, User, Partenariat
# Create your views here.

def home(request):
    articles = Article.objects.all()
    actions = Projet.objects.all()
    return render(request, 'home.html', {'articles':articles, 'actions':actions})

def about(request):
    actions = Projet.objects.all()
    return render(request, 'about.html', {'actions':actions})

def team(request):
    
    return render(request, 'team.html')

def gallery(request):
    albums = Album.objects.all()
    return render(request, 'gallery.html', {'albums':albums})

def gallery_details(request, id):
    album = Album.objects.get(id=id)
    photos = album.images.all()
    return render(request, 'gallery_details.html', {'album':album, 'photos':photos})

def ressources(request):
    ressources = Ressource.objects.all()
    return render(request, 'ressources.html', {'ressources':ressources})

def actions(request):
    actions = Projet.objects.all()
    return render(request, 'actions.html', {'actions':actions})

def action_details(request, action_id):
    action = Projet.objects.get(id = action_id)
    return render(request, 'action_details.html', {'action':action})

def news(request):
    articles = Article.objects.all()
    return render(request, 'news.html', {'articles':articles})

def news_details(request, article_id):
    article = Article.objects.get(id = article_id)
    return render(request, 'news_details.html', {'article':article})

def contact(request):
    return render(request, 'contact.html')


#Demande de patenariat views
def demande_partenariat(request):
    if request.method == 'POST':
        Partenariat.objects.create(
            type_partenariat=request.POST.get('type_partenariat'),
            nom_organisation=request.POST.get('nom_organisation'),
            nom=request.POST.get('nom'),
            pays=request.POST.get('pays'),
            ville=request.POST.get('ville'),
            prenom=request.POST.get('prenom'),
            email=request.POST.get('email'),
            telephone=request.POST.get('telephone'),
            objet=request.POST.get('objet'),
            message=request.POST.get('message'),
            document=request.FILES.get('document')
        )
        messages.success(request, "Votre demande a été envoyée avec succès.")
        return redirect(request.META.get('HTTP_REFERER'))


#Demande de bénévolat views
def demande_benevolat(request):
    if request.method == 'POST':
        Benevole.objects.create(
            nom=request.POST.get('nom'),
            prenom=request.POST.get('prenom'),
            email=request.POST.get('email'),
            contact=request.POST.get('contact'),
            pays=request.POST.get('pays'),
            ville=request.POST.get('ville'),
            competences=request.POST.get('competences'),
            message=request.POST.get('message'),
            cv=request.FILES.get('cv')
        )
        messages.success(request, "Votre demande a été envoyée avec succès.")
        return redirect(request.META.get('HTTP_REFERER'))


