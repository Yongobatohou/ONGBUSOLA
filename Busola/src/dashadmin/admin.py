from django.contrib import admin
# Register your models here.
from .models import (
    User, Article, CategorieArticle, Projet,
    Album, Galerie, Ressource, Benevole, Partenariat
)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'nom', 'prenom', 'email', 'role')
    search_fields = ('nom', 'prenom', 'email')


@admin.register(CategorieArticle)
class CategorieArticleAdmin(admin.ModelAdmin):
    list_display = ('nom', 'auteur', 'date_creation', 'date_modification')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'auteur', 'date_pub', 'image', 'date_modification')
    list_filter = ('categorie', 'auteur')
    search_fields = ('titre', 'contenu')


@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ('nom', 'secteur', 'montant_financement', 'statut', 'date_creation', 'date_modification')


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description','auteur', 'date_pub', 'image', 'date_modification')


@admin.register(Galerie)
class GalerieAdmin(admin.ModelAdmin):
    list_display = ('album', 'image', 'date_creation', 'date_modification')


@admin.register(Ressource)
class RessourceAdmin(admin.ModelAdmin):
    list_display = ('intitule', 'date_creation', 'date_modification')
    search_fields = ('intitule',)

@admin.register(Benevole)
class BenevoleAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'contact', 'statut', 'date_submission')
    list_filter = ('statut', 'date_submission')
    search_fields = ('nom', 'prenom', 'email', 'organisation')



@admin.register(Partenariat)
class PartenariatAdmin(admin.ModelAdmin):

    list_display = (
        'nom',
        'prenom',
        'type_partenariat',
        'email',
        'telephone',
        'statut',
        'date_soumission'
    )

    list_filter = (
        'type_partenariat',
        'statut',
        'date_soumission'
    )

    search_fields = (
        'nom',
        'prenom',
        'email',
        'nom_organisation'
    )

    readonly_fields = (
        'date_soumission',
        'date_traitement'
    )

    fieldsets = (
        ('Type de partenariat', {
            'fields': ('type_partenariat', 'statut')
        }),
        ('Informations du demandeur', {
            'fields': (
                'nom', 'prenom', 'email', 'telephone',
                'pays', 'ville', 'nom_organisation'
            )
        }),
        ('Contenu de la demande', {
            'fields': ('objet', 'message', 'document')
        }),
        ('Suivi interne', {
            'fields': ('date_soumission', 'date_traitement')
        }),
    )

    ordering = ('-date_soumission',)
