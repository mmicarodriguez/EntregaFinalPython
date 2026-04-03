from django.urls import path
from .views import PageListView, PageDetailView, PageUpdateView
from .views import home
from .views import about
from .views import SignUpView
from .views import PageDeleteView
from .views import PageCreateView

urlpatterns = [
    path('pages/', PageListView.as_view(), name='pages'),
    path('pages/<int:pk>/', PageDetailView.as_view(), name='detail'),
    path('pages/<int:pk>/editar/', PageUpdateView.as_view(), name='edit'),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('pages/<int:pk>/delete/', PageDeleteView.as_view(), name='delete'),
    path('pages/crear/', PageCreateView.as_view(), name='create'),
]