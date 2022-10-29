from django.http import JsonResponse
from .Tools import getAllCompany

def ping(request):
    data = {'ping': 'pong!'}
    return JsonResponse(data)

def getAllListedCompany(request):
    return JsonResponse(getAllCompany())