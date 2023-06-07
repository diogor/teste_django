from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.views.generic.edit import UpdateView, DeleteView
from .mixins import UserIsAdminMixin
from .forms import UserCreationForm, UserEditForm
from .models import User


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        return super().form_valid(form)


class ListUserView(UserIsAdminMixin, ListView):
    model = User
    paginate_by = 20
    template_name = "user_list.html"


class DetailUserView(UserIsAdminMixin, UpdateView):
    form_class = UserEditForm
    model = User
    template_name = "user_form.html"
    success_url = reverse_lazy("list_user")


class DeleteUserView(UserIsAdminMixin, DeleteView):
    model = User
    success_url = reverse_lazy("list_user")
    template_name = "user_delete.html"
