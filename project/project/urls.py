from django.contrib import admin
from django.urls import path as p, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.conf import settings
from django.conf.urls.static import static

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

urlpatterns = [
    p('admin/', admin.site.urls),
    p('', include('blog.urls')),
    p('', include('messaging.urls')),
    p('signup/', SignUpView.as_view(), name='signup'),
    p('accounts/', include('accounts.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    p('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    p('logout/', auth_views.LogoutView.as_view(), name='logout'),
]