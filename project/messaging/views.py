from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Mensaje

class MensajeCreateView(CreateView):
    model = Mensaje
    fields = ['nombre', 'email', 'contenido']
    template_name = 'messaging/form.html'
    success_url = reverse_lazy('pages')
