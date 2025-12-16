
from django.contrib import admin
from django.urls import path
from dashadmin import views
from django.conf.urls import handler404, handler500

handler404 = 'dashadmin.views.custom_404'
handler500 = 'dashadmin.views.custom_500'

urlpatterns = [
    path('', views.index, name='index'),
    # Users views
    path('users/users-list/', views.users_list, name='users-list'),
    path('users/users-add/', views.users_add, name='users-add'),
    path('users/users-update/', views.users_update, name='users-update'),
    path('users/users-delete/', views.users_delete, name='users-delete'),
    # Catégories d'articles views
    path('categories/categories-list/', views.categories_list, name='categories-list'),
    path('categories/categories-add/', views.categorie_add, name='categories-add'),
    path('categories/edit/<int:id>/', views.categorie_edit, name='edit_categorie'),
    path('categories/categories-update/<int:categorie_id>/', views.categories_update, name='categories-update'),
    path('categories/categories-delete/<int:categorie_id>/', views.categories_delete, name='categories-delete'),
    # Articles views
    path('articles/articles-list/', views.articles_list, name='articles-list'),
    path('articles/articles-add/', views.article_add, name='articles-add'),
    path('articles/edit/<int:id>/', views.article_edit, name='edit_article'),
    path('articles/articles-update/<int:article_id>/', views.articles_update, name='articles-update'),
    path('articles/articles-delete/<int:article_id>/', views.articles_delete, name='articles-delete'),
    # Projets views
    path('projets/projets-list/', views.projets_list, name='projets-list'),
    path('projets/projets-add/', views.projets_add, name='projets-add'),
    path('projets/projets-edit/<int:project_id>/', views.projets_edit, name='projets-edit'),
    path('projets/projets-update/<int:project_id>/', views.projets_update, name='projets-update'),
    path('projets/projets-delete/<int:project_id>/', views.projets_delete, name='projets-delete'),

    # Benevoles views
    path('benevoles/benevoles-list/', views.benevoles_list, name='benevoles-list'),
    path('benevoles/benevoles-read/<int:id>/', views.benevoles_read, name='benevoles_read'),
    path('benevoles/benevoles-delete/<int:id>/', views.benevoles_delete, name='benevoles_delete'),


    # Partenariat views
    path('partenaires/partenaires-list/', views.partenariats_list, name='partenaires-list'),
    path('partenaires/partenaires-read/<int:id>/', views.partenariats_read, name='partenaires_read'),
    path('partenaires/partenaires-delete/<int:id>/', views.partenariats_delete, name='partenaires_delete'),



    # Ressources views
    path('ressources/ressources-list/', views.ressources_list, name='ressources-list'),
    path('ressources/ressources-add/', views.ressources_add, name='ressources-add'),
    path('ressources/ressources-edit/<int:id>/', views.ressources_edit, name='ressources-edit'),
    path('ressources/ressources-update/<int:id>/', views.ressources_update, name='ressources-update'),
    path('ressources/ressources-delete/<int:id>/', views.ressources_delete, name='ressources-delete'),

     # Albums views
    path('albums/albums-list/', views.albums_list, name='albums-list'),
    path('albums/albums-add/', views.albums_add, name='albums-add'),
    path('albums/views/<int:id>/', views.album_view, name='details_album'),
    path('albums/edit/<int:id>/', views.albums_edit, name='edit_album'),
    path('albums/albums-update/<int:id>/', views.albums_update, name='albums-update'),
    path('albums/albums-delete/<int:id>/', views.albums_delete, name='albums-delete'),
        #PHOTOS VIEWS
    path('albums/add-photo/<int:id>/', views.photos_add, name='photo-add'),
    path('albums/delete-photo/<int:id>/', views.photos_delete, name='photo-delete')
]   