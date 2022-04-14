from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from getTax.taxcal import taxCalculator


# Create your views here.
def index(request):
    return render(request, 'index.html')
def submitquerry(request):
    salary = int(request.GET['Salary_income'])
    FOtrading = int(request.GET['FO_trading'])
    intraday = int(request.GET['Intraday_Trading'])
    STCGain = int(request.GET['Short_Term_Capital_Gain'])
    intrestgain = int(request.GET['intrest_income'])
    lossGain = int(request.GET['loss_Gain'])
    taxobj = taxCalculator(salary, FOtrading, intraday, STCGain, intrestgain, lossGain)
    totaltax = taxobj.calculateTax()
    DATASet = {
        'tax' : totaltax,
        'errorStatus' : True
    }
    
    return render(request, 'index.html', context=DATASet)
