from django.urls import path
from .views import MensajeCreateView

urlpatterns = [
    path('mensaje/', MensajeCreateView.as_view(), name='mensaje'),
]