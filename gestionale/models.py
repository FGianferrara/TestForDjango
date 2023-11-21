from django.db import models

# Create your models here.
class Esame(models.Model):
    id = models.AutoField               (primary_key = True)
    data = models.DateTimeField         () 
    tipo = models.CharField             (max_length = 255)
    esito = models.CharField            (max_length = 255)
    struttura = models.CharField        (max_length = 255, default = 'PROVA')
    file_referto = models.FileField     (null = True)
    cda2 = models.TextField             (null = True)
    paziente = models.ForeignKey        ('Paziente',null = True, on_delete=models.CASCADE)
    unita_misura=models.CharField       (max_length=20, null=True)
    valore= models.IntegerField         (null = True)



class Paziente(models.Model):
    codice_fiscale = models.CharField   (max_length=16)
    nome = models.CharField             (max_length=255)
    cognome = models.CharField          (max_length=255)