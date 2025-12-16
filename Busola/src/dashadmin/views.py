from django.shortcuts import render, redirect
import os
from dashadmin.models import Article, CategorieArticle, Projet, Album, Galerie, Ressource, Benevole, User, Partenariat
# Create your views here.


def custom_404(request, exception):
    return render(request, 'error-404.html', status=404)

def custom_500(request):
    return render(request, 'error-500.html', status=500)


def index(request):
    article = Article.objects.count()    
    return render(request, 'index.html', {'article':article})

# Users views
def users_list(request):
    users = User.objects.all()
    return render(request, 'users/user-list.html', {'users':users})  

def users_add(request):
    return render(request, 'users/user-add.html')

def users_update(request):
    return render(request, 'users/user-update.html')

def users_delete(request):
    return render(request, 'users/user-delete.html')

# Articles views
def articles_list(request):
    articlesCat = CategorieArticle.objects.all()
    articles = Article.objects.all()
    return render(request, 'articles/articles.html', {'categories':articlesCat, 'articles':articles})

def article_add(request):
    if request.method == "POST":
        titre = request.POST.get('titre')
        extrait = request.POST.get('extrait')
        image = request.FILES.get('image')
        categorie = request.POST.get('categorie')
        contenu = request.POST.get('contenu')
        statut = request.POST.get('publier')
        Article.objects.create(titre = titre, extrait = extrait, image = image, categorie_id=categorie, contenu=contenu, statut=statut)
        return redirect('articles-list')

def article_edit(request, id):
    article = Article.objects.get(id=id)
    categories = CategorieArticle.objects.all()
    return render(request, 'articles/article_edit.html', {'article':article, 'categories':categories})

def articles_update(request, article_id):
    article = Article.objects.get(id = article_id)
    categorie = request.POST.get('categorie')
    data = {
        "titre" : request.POST.get('titre'),
        "extrait" : request.POST.get('extrait'),
        "categorie_id" : CategorieArticle.objects.get(id = categorie),
        "contenu" : request.POST.get('contenu'),
        "statut" : request.POST.get('publier')
    }
    for key, value in data.items():
        setattr(article, key, value)

    if request.FILES.get('image'):
            # Supprimer l’ancienne image
            if article.image and article.image.path:
                if os.path.isfile(article.image.path):
                    os.remove(article.image.path)

            # Attribuer la nouvelle image
            article.image = request.FILES.get('image')
    article.save()
    return redirect('articles-list')

def articles_delete(request, article_id):
    article = Article.objects.get(id = article_id)
    if article.image and article.image.path:
        if os.path.isfile(article.image.path):
            os.remove(article.image.path)
    article.delete()
    return redirect('articles-list')


# Catégories views
def categories_list(request):
    categories = CategorieArticle.objects.all()
    return render(request, 'articles/categories.html', {'categories':categories})

def categorie_add(request):
    if request.method == "POST":
        nom = request.POST.get('nom')
        CategorieArticle.objects.create(nom = nom)
        return redirect('categories-list')

def categorie_edit(request, id):
    categorie = CategorieArticle.objects.get(id=id)
    return render(request, 'articles/categorie_edit.html', {'categorie':categorie})

def categories_update(request, categorie_id):
    categorie = CategorieArticle.objects.get(id = categorie_id)
    data = {
        "nom" : request.POST.get('nom'),
    }
    for key, value in data.items():
        setattr(categorie, key, value)

    categorie.save()
    return redirect('categories-list')

def categories_delete(request, categorie_id):
    categorie = CategorieArticle.objects.get(id = categorie_id)
    categorie.delete()
    return redirect('categories-list')


# Projets views
def projets_list(request):
    projets = Projet.objects.all()
    return render(request, 'projets/projects.html', {'projets':projets})

def projets_add(request):
    if request.method == "POST":
        nom = request.POST.get('nom')
        secteur = request.POST.get('secteur')
        description = request.POST.get('description')
        details = request.POST.get('details')
        partenaires = request.POST.get('partenaires')
        taux = request.POST.get('taux')
        image = request.FILES.get('image')
        tdr = request.FILES.get('tdr')
        montant_financement = request.POST.get('montant_financement')
        statut = request.POST.get('publier')
        Projet.objects.create(nom = nom, secteur = secteur, description = description, details = details, partenaires = partenaires, taux = taux, image = image, tdr = tdr, montant_financement = montant_financement, statut = statut)
        return redirect('projets-list')

def projets_edit(request, project_id):
    project = Projet.objects.get(id = project_id)
    return render(request, 'projets/project_edit.html', {'project':project})

def projets_update(request, project_id):
    project = Projet.objects.get(id = project_id)
    data = {
        "nom" : request.POST.get('nom'),
        "secteur" : request.POST.get('secteur'),
        "description" : request.POST.get('description'),
        "details" : request.POST.get('details'),
        "partenaires" : request.POST.get('partenaires'),
        "taux" : request.POST.get('taux'),
        "montant_financement" : request.POST.get('montant_financement'),
        "statut" : request.POST.get('publier')
    }
    for key, value in data.items():
        setattr(project, key, value)
    if request.FILES.get('tdr'):
        project.tdr = request.FILES.get('tdr')
    if request.FILES.get('image'):
        project.image = request.FILES.get('image')
    project.save()
    return redirect('projets-list')

def projets_delete(request, project_id):
    project = Projet.objects.get(id = project_id)
    if project.tdr and project.tdr.path:
        if os.path.isfile(project.tdr.path):
            os.remove(project.tdr.path)
    if project.image and project.image.path:
        if os.path.isfile(project.image.path):
            os.remove(project.image.path)
    project.delete()
    return redirect('projets-list')



# Benevoles views
def partenariats_list(request):
    partenariats = Partenariat.objects.all()
    return render(request, 'benevole/partenaires.html', {'partenaires':partenariats})

def partenariats_read(request, id):
    partenariat = Partenariat.objects.get(id = id)
    return render(request, 'benevole/partenaire_details.html', {'partenariat':partenariat})

def partenariats_delete(request, id):
    partenaire = Partenariat.objects.get(id = id)
    if partenaire.document and partenaire.url.path:
        if os.path.isfile(partenaire.url.path):
            os.remove(partenaire.url.path)
    partenaire.delete()
    return redirect('partenariats-list')



# Benevoles views
def benevoles_list(request):
    benevoles = Benevole.objects.all()
    return render(request, 'benevole/benevoles.html', {'benevoles':benevoles})

def benevoles_read(request, id):
    benevole = Benevole.objects.get(id = id)
    return render(request, 'benevole/benevole_details.html', {'partenariat':benevole})

def benevoles_delete(request, id):
    benevole = Benevole.objects.get(id = id)
    if benevole.cv and benevole.url.path:
        if os.path.isfile(benevole.url.path):
            os.remove(benevole.url.path)
    benevole.delete()
    return redirect('benevoles-list')


# Users profile views
def users_profile(request):
    return render(request, 'users/user-profile.html')



# Ressources views
def ressources_list(request):
    ressources = Ressource.objects.all()
    return render(request, 'ressources/ressources.html', {'ressources':ressources})

def ressources_add(request):
    if request.method == "POST":
        intitule = request.POST.get('intitule')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        url = request.FILES.get('url')
        statut = request.POST.get('publier')
        Ressource.objects.create(intitule = intitule, description = description, image = image, url = url, statut = statut)
        return redirect('ressources-list')

def ressources_edit(request, id):
    ressource = Ressource.objects.get(id=id)
    return render(request, 'ressources/ressource_edit.html', {'ressource':ressource})

def ressources_update(request, id):
    ressource = Ressource.objects.get(id = id)
    data = {
        "intitule" : request.POST.get('intitule'),
        "description" : request.POST.get('description'),
        "statut" : request.POST.get('publier')
    }
    for key, value in data.items():
        setattr(ressource, key, value)
    if request.FILES.get('url'):
        ressource.url = request.FILES.get('url')
    if request.FILES.get('image'):
        ressource.image = request.FILES.get('image')
    ressource.save()
    return redirect('ressources-list')

def ressources_delete(request, id):
    ressource = Ressource.objects.get(id = id)
    if ressource.tdr and ressource.url.path:
        if os.path.isfile(ressource.url.path):
            os.remove(ressource.url.path)
    if ressource.image and ressource.image.path:
        if os.path.isfile(ressource.image.path):
            os.remove(ressource.image.path)
    ressource.delete()
    return redirect('ressources-list')


#Albums views

def albums_list(request):
    albums = Album.objects.all()
    return render(request, 'albums/albums.html', {'albums':albums})

def albums_add(request):
    if request.method == "POST":
        nom = request.POST.get('nom')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        auteur = request.user.id
        Album.objects.create(nom = nom, description = description, image = image, auteur = auteur)
        return redirect('albums-list')

def album_view(request, id):
    album = Album.objects.get(id=id)
    photos = album.images.all()
    return render(request, 'albums/album_details.html', {'album':album, 'photos':photos})

def albums_edit(request, id):
    album = Album.objects.get(id=id)
    return render(request, 'albums/album_edit.html', {'album':album})

def albums_update(request, id):
    album = Album.objects.get(id = id)
    data = {
        "nom" : request.POST.get('nom'),
        "description" : request.POST.get('description'),
    }
    for key, value in data.items():
        setattr(album, key, value)
    if request.FILES.get('image'):
        album.image = request.FILES.get('image')
    album.save()
    return redirect('albums-list')

def albums_delete(request, id):
    album = Album.objects.get(id = id)
    if album.image and album.image.path:
        if os.path.isfile(album.image.path):
            os.remove(album.image.path)
    albums.delete()
    return redirect('albums-list')



# Photos views

def photos_add(request, id):
    album = Album.objects.get(id = id)
    photos = album.images.all()
    if request.method == "POST":
        image = request.FILES.get('image')
        album_id = album.id
        Galerie.objects.create(image = image, album_id = album_id)
    
    return render(request, 'albums/album_details.html', {
        'album': album,
        'photos': photos
    })

def photos_delete(request, id):
    photo = Galerie.objects.get(id = id)
    album = Album.objects.get(id = photo.album_id)
    photos = album.images.all()
    if photo.image and photo.image.path:
        if os.path.isfile(photo.image.path):
            os.remove(photo.image.path)
    photo.delete()
    return render(request, 'albums/album_details.html', {
        'album': album,
        'photos': photos
    })