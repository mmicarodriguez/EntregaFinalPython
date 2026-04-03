from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Page
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

class PageListView(ListView):
    model = Page
    template_name = 'blog/pages.html'

class PageDetailView(DetailView):
    model = Page
    template_name = 'blog/page_detail.html'

class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen', 'fecha']
    template_name = 'blog/page_form.html'
    success_url = reverse_lazy('pages')

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'blog/signup.html'
    success_url = reverse_lazy('login')

class PageDeleteView(LoginRequiredMixin, DeleteView):
        model = Page
        template_name = 'blog/page_confirm_delete.html'
        success_url = reverse_lazy('pages')

class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen', 'fecha']
    template_name = 'blog/page_form.html'
    success_url = reverse_lazy('pages')