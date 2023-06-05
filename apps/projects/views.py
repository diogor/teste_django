from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from .models import Project


class ProjectCreate(PermissionRequiredMixin, CreateView):
    model = Project
    fields = ["name", "image", "description"]
    success_url = reverse_lazy("project_list")
    permission_required = "projects.add_project"


class ProjectList(PermissionRequiredMixin, ListView):
    model = Project
    paginate_by = 20
    permission_required = "projects.view_project"
    template_name = "project_list.html"
