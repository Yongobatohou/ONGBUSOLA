"""
URL configuration for ONGBUSOLA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from ONGBUSOLA import settings
from django.conf.urls.static import static
from django.urls import path, include
from ONGBUSOLA import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dash/', include('dashadmin.urls')),

    path('', views.home, name='home'),

    path('about/', views.about, name='about'),
    path('team/', views.team, name='team'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery_details/<int:id>', views.gallery_details, name='gallery_details'),
    path('ressources/', views.ressources, name='ressources'),

    path('actions/', views.actions, name='actions'),
    path('action_details/<int:action_id>/', views.action_details, name='action_details'),

    path('news/', views.news, name='news'),
    path('news_details/<int:article_id>/', views.news_details, name='news_details'),
    path('contact/', views.contact, name='contact'),

    path('demande/partenariat/', views.demande_partenariat, name='demande_partenariat'),
    path('demande/benevolat/', views.demande_benevolat, name='demande_benevolat')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
