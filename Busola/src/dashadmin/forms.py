from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'extrait', 'contenu', 'image', 'videos', 'categorie', 'auteur']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'extrait': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'contenu': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'categorie': forms.Select(attrs={'class': 'form-select'}),
            'auteur': forms.Select(attrs={'class': 'form-select'}),
        }
