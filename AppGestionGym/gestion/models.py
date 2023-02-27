from django.db import models

# Create your models here.

class Personne(models.Model):
    prenom_text = models.CharField('Prénom', max_length=100)
    nom_text = models.CharField('Nom', max_length=100)
    naissance_date = models.DateField('Date de naissance')
    mail_email = models.EmailField('Adresse mail')
    telephone_integer = models.PositiveIntegerField('Numéro de téléphone', blank=True, null=True)
    def __str__(self):
        return self.prenom_text + " " + self.nom_text

class Encadrant(models.Model):
    personne = models.OneToOneField(Personne, on_delete=models.CASCADE)
    def __str__(self):
        return self.personne.prenom_text + " " + self.personne.nom_text

class Adherent(models.Model):
    personne = models.OneToOneField(Personne, on_delete=models.CASCADE)
    appreciation_text = models.CharField('Appréciation', max_length=500, blank=True)
    def __str__(self):
        return self.personne.prenom_text + " " + self.personne.nom_text

class Groupe(models.Model):
    adherent_list = models.ManyToManyField(Adherent)
    encadrant_list = models.ManyToManyField(Encadrant)
    nom_groupe_text = models.CharField('Nom du groupe', max_length=100)
    def __str__(self):
        return self.nom_groupe_text

class Cours(models.Model):
    groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)
    horaire_date = models.DateTimeField('Date et heure')
    duree_time = models.TimeField('Durée')
    def __str__(self):
        return self.groupe.nom_groupe_text
