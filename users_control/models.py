from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Enseignant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    departement = models.CharField(max_length=50)
    grade = models.CharField(max_length=50)
    salaire = models.FloatField()


class Theme(models.Model):
    num = models.IntegerField()
    titre = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    keyword = models.CharField(max_length=50)
    difficulte = models.CharField(max_length=50)
    domaine = models.CharField(max_length=50)


class Etudiant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    specialite = models.CharField(max_length=50)
    promotion = models.CharField(max_length=50)
    niveau = models.CharField(max_length=50)


class ChefSep(models.Model):
    enseignant = models.OneToOneField(Enseignant, on_delete=models.CASCADE)
    salaire = models.FloatField()
    role = models.CharField(max_length=25)
