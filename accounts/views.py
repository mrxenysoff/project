from django.views.generic import TemplateView
#from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from .forms import UserCreationForm

class HomePageView(TemplateView):
    template_name = 'accounts/home.html'

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # перенаправляет в случае успешного логирования
    template_name = 'accounts/signup.html'




class AboutView(TemplateView):
    template_name = 'accounts/about.html'

