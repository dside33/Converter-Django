from django import forms

class ExchangeForm(forms.Form):
    inputAmount = forms.CharField(label='Введите сумму:', max_length=7)
    from_curr = forms.ChoiceField(label='Из валюты', choices=[])
    to_curr = forms.ChoiceField(label='В валюту')

    def __init__(self, *args, **kwargs):
        context = kwargs.pop('data', None)
        super(ExchangeForm, self).__init__(*args, **kwargs)
        if context:
            currencies = context.get('currencies', {})
            self.fields['from_curr'].choices = [(currency, currency) for currency in currencies]
            self.fields['to_curr'].choices = [(currency, currency) for currency in currencies]