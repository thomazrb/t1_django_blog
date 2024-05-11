from django.urls import path
from .views import soma_numeros

urlpatterns = [
    path('', soma_numeros, name='soma'),
]
