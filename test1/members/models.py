from django.db import models
from django.contrib.auth.models import User
from django import forms

class Member (models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

#Ajout de la classe Cooperative
class Cooperative(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    date_creation = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nom

# Ajout de la classe Membre qui herite de la classe User

class Membre(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cooperative = models.ForeignKey(Cooperative, related_name='membres',on_delete=models.CASCADE)
    adresse = models.CharField(max_length=255)
    numero_identification = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username