from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser

# ============================
#   CUSTOM USER MODEL
# ============================
class User(AbstractUser):
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    post = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)
    role = models.CharField(max_length=80, blank=True, null=True
    , choices=[('admin', 'Admin'), ('editor', 'Editor'), ('user', 'User')])
    statut = models.CharField(max_length=80, blank=True, null=True
    , choices=[('active', 'Active'), ('inactive', 'Inactive')])
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nom', 'prenom', 'role']

    def __str__(self):
        return f"{self.prenom} {self.nom}"


# ============================
#   CATEGORIE ARTICLES
# ============================
class CategorieArticle(models.Model):
    nom = models.CharField(max_length=255, unique=True)
    auteur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom


# ============================
#   ARTICLE
# ============================
class Article(models.Model):
    titre = models.CharField(max_length=255)
    extrait = models.TextField()
    contenu = models.TextField()
    image = models.ImageField(upload_to='articles/images/', null=True, blank=True)
    videos = models.FileField(upload_to='articles/videos/', null=True, blank=True)
    categorie = models.ForeignKey(CategorieArticle, on_delete=models.SET_NULL, null=True)
    auteur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=80, blank=True, null=True
    , choices=[('publier', 'Publier'), ('non_publier', 'Non publier')])
    date_modification = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.titre


# ============================
#   PROJETS
# ============================
class Projet(models.Model):
    secteur = models.CharField(max_length=255)
    nom = models.CharField(max_length=255)
    partenaires = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    taux = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='projets/images/', null=True, blank=True)
    tdr = models.FileField(upload_to='projets/tdr/', null=True, blank=True)
    montant_financement = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    details = models.TextField(blank=True, null=True)
    statut = models.CharField(max_length=80, blank=True, null=True
    , choices=[('publier', 'Publier'), ('non_publier', 'Non publier')])
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nom


# ============================
#   ALBUM
# ============================
class Album(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='albums/', null=True, blank=True)
    auteur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_modification = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nom


# ============================
#   GALERIE
# ============================
class Galerie(models.Model):
    album = models.ForeignKey(Album, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='galerie/')
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Image de {self.album.nom}"


# ============================
#   RESSOURCES
# ============================
class Ressource(models.Model):
    intitule = models.CharField(max_length=255)
    image = models.ImageField(upload_to='ressources/images/', null=True, blank=True)
    description = models.TextField()
    url = models.FileField(upload_to='ressources/fichiers/', null=True, blank=True)
    statut = models.CharField(max_length=80, blank=True, null=True
    , choices=[('publier', 'Publier'), ('non_publier', 'Non publier')])
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True) 
    def __str__(self):
        return self.intitule


# ============================
#   MEMBERS
# ============================
class Member(models.Model):
    nom = models.CharField(max_length=100)
    poste = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='team/')
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True) 
    def __str__(self):
        return self.intitule



class Partenariat(models.Model):

    TYPE_PARTENARIAT_CHOICES = [
        ('financier', 'Partenariat financier'),
        ('technique', 'Partenariat technique'),
        ('institutionnel', 'Partenariat institutionnel'),
        ('benevole', 'Bénévolat / Engagement personnel'),
        ('autre', 'Autre'),
    ]

    STATUT_CHOICES = [
        ('nouvelle', 'Nouvelle'),
        ('en_cours', 'En cours de traitement'),
        ('acceptee', 'Acceptée'),
        ('refusee', 'Refusée'),
    ]

    # Informations générales
    type_partenariat = models.CharField(
        max_length=30,
        choices=TYPE_PARTENARIAT_CHOICES
    )

    nom_organisation = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        help_text="Nom de l'organisation ou institution"
    )

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    email = models.EmailField()
    telephone = models.CharField(max_length=30)

    pays = models.CharField(max_length=100, blank=True, null=True)
    ville = models.CharField(max_length=100, blank=True, null=True)

    # Contenu de la demande
    objet = models.CharField(max_length=200)
    message = models.TextField()
    # Pièce jointe optionnelle
    document = models.FileField(
        upload_to='partenariats/',
        blank=True,
        null=True
    )
    # Suivi
    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default='nouvelle'
    )
    # Métadonnées
    date_soumission = models.DateTimeField(auto_now_add=True)
    date_traitement = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-date_soumission']
        verbose_name = "Partenariat"
        verbose_name_plural = "Partenariat"

    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.get_type_partenariat_display()}"




# ============================
#   BENEVOLES
# ============================
class Benevole(models.Model):

    STATUT_CHOICES = [
        ('nouveau', 'Nouvelle demande'),
        ('en_attente', 'En attente'),
        ('valide', 'Validée'),
        ('refuse', 'Refusée'),
    ]

    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    email = models.EmailField()
    contact = models.CharField(max_length=50)
    pays = models.CharField(max_length=100, blank=True, null=True)
    ville = models.CharField(max_length=100, blank=True, null=True)
    competences = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    cv = models.FileField(
        upload_to='bénévoles/',
        blank=True,
        null=True
    )
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='nouveau')
    date_submission = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"