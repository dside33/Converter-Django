from django.shortcuts import render
import requests

from exchange.forms import ExchangeForm


def exchange(request):
    api_url = 'https://api.exchangerate-api.com/v4/latest/USD'
    response = requests.get(url=api_url).json()

    data = response.get('rates')
    if request.method == 'GET':
        form = ExchangeForm(data = {'currencies': data})
        context = {
            'currencies': data,
            'form': form
        }

        # print(data)
        return render(request, 'exchange/index.html', context=context)

    if request.method == 'POST':
        form = ExchangeForm(request.POST, data={'currencies': data})
        if form.is_valid():
            amount = float(form.cleaned_data['inputAmount'])
            from_curr = form.cleaned_data['from_curr']
            to_curr = form.cleaned_data['to_curr']

            converted_amount = round((data[to_curr] / data[from_curr]) * amount, 2)

            context = {
                'amount': amount,
                'from_curr': from_curr,
                'to_curr': to_curr,
                'currencies': data,
                'converted_amount': converted_amount,
                'form': form
            }

            return render(request, 'exchange/index.html', context=context)

    # data = {'currencies': {'USD': 1, 'AED': 3.67}}  # Пример списка валют
    # form = ExchangeForm(context = data)
    # return render(request, 'exchange/index.html', context={'form': form})