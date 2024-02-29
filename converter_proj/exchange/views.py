from django.shortcuts import render
import requests
from rest_framework import status

from exchange.forms import ExchangeForm


def exchange(request):
    # api_url = 'https://api.exchangerate-api.com/v4/latest/USD'
    # response = requests.get(url=api_url).json()

    # data = response.get('rates')
    # if request.method == 'GET':
    #     context = {
    #         'currencies': data
    #     }

    #     print(data)
    #     return render(request, 'exchange/index.html', context=context)

    # if request.method == 'POST':
    #     amount = float(request.POST.get('amount'))
    #     from_curr = request.POST.get('from_curr')
    #     to_curr = request.POST.get('to_curr')

    #     converted_amount = round((data[to_curr]/ data[from_curr]) * amount, 2)

    #     context = {
    #         'amount': amount,
    #         'from_curr': from_curr,
    #         'to_curr': to_curr,
    #         'currencies': data,
    #         'converted_amount': converted_amount
    #     }

    #     print(context)
    #     return render(request, 'exchange/index.html', context=context)

    form = ExchangeForm()
    return render(request, 'exchange/index.html', context={'form': form})