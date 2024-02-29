from django import forms

class ExchangeForm(forms.Form):
    inputAmount = forms.CharField(label='Введите сумму:', max_length=7)
    from_curr = forms.ChoiceField(label='Из валюты')
    to_curr = forms.ChoiceField(label='В валюту')