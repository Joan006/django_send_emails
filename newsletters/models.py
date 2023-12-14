from django.db import models
"""Creacion modelo -> agregar migraciones == agrega base datos"""

# Modelo user
class NewsletterUser(models.Model):
    email = models.EmailField(null=False, unique=True)
    date_addet = models.DateTimeField(auto_now_add=True)
    # se guarada automaticamente la fecha de la creacion
    
    def __str__(self):
        return self.email


# Modelo NewsletterUser
class Newsletter(models.Model):
    name = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    body = models.TextField(blank=True, null=True)
    # permite que el mail se pueda enviar con el body vacio
    email = models.ManyToManyField(NewsletterUser)
    # Relacion entre modelos 
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

