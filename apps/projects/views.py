from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from .models import Project


class ProjectCreate(PermissionRequiredMixin, CreateView):
    model = Project
    fields = ["name", "image", "description"]
    success_url = reverse_lazy("list_project")
    permission_required = "projects.add_project"
    template_name = "project_form.html"


class ProjectList(PermissionRequiredMixin, ListView):
    model = Project
    paginate_by = 20
    permission_required = "projects.view_project"
    template_name = "project_list.html"


class ProjectDetail(PermissionRequiredMixin, DetailView):
    model = Project
    permission_required = "projects.view_project"
    template_name = "project_detail.html"


class ProjectDelete(PermissionRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy("list_project")
    permission_required = "projects.delete_project"
    template_name = "project_delete.html"
