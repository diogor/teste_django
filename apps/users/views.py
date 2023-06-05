from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserCreationForm


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "register.html"
    success_url = reverse_lazy("login")
