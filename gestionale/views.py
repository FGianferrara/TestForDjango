import datetime
from random import randint
from django.http import HttpResponse, JsonResponse
from gestionale.models import (Esame, Paziente)

def index(request):
    id=request.GET.get('id')
    #tipo=request.GET.get('tipo')
    p = Paziente.objects.get(id=id)

    p.codice_fiscale = 'TEST'
    p.nome = 'Pino'
    p.cognome = 'Daniele'
    p.save()

    esame = Esame()
    
    esame.data = datetime.datetime.now()
    esame.tipo = 'test'
    esame.esito = 'test'
    esame.struttura = 'struttura2'
    esame.valore = randint(4,15)
    esame.unita_misura = 'mg'
    esame.paziente = p
    esame.save()

    return HttpResponse("New ")

def index_2(request):
    esami = Esame.objects.all()
    result = []
    for esame in esami:
        result.append({
            'data_e_ora':(str(esame.data)),
            'tipo': esame.tipo,
            'valore': esame.valore,
            #'paziente': esame.paziente,
            }
            )

    return JsonResponse(result, safe = False)