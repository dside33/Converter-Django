from django.urls import path
from exchange.views import exchange

urlpatterns = [
    path('', exchange)
]
