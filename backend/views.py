from django.http import JsonResponse
from .Tools import getAllCompany , getCompanyData , getPeriodicCompanyData

def ping(request):
    data = {'ping': 'pong!'}
    return JsonResponse(data)

def getAllListedCompany(request):
    return JsonResponse(getAllCompany())

def getCompanywiseData(request):
   return JsonResponse(getCompanyData(request.GET.get("company"),request.GET.get("start_date"),request.GET.get("end_date")))

def getPeriodicComapnywiseData(request):
    return JsonResponse(getPeriodicCompanyData(request.GET.get("company"),request.GET.get("period"),request.GET.get("interval")))
