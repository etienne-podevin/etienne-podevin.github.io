from django.contrib import admin

from .models import Personne, Adherent, Encadrant, Groupe, Cours

admin.site.register(Personne)
admin.site.register(Adherent)
admin.site.register(Encadrant)
admin.site.register(Groupe)
admin.site.register(Cours)