from django.shortcuts import render
from .utils import get_crypto_data  # remove get_coin_details if not used
from django.http import JsonResponse

def index(request):
    coins = get_crypto_data()
    return render(request, 'index.html', {'coins': coins})

def crypto_data_api(request):
    coins = get_crypto_data()
    return JsonResponse({'coins': coins})
