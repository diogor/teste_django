"""
URL configuration for teste_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import ProjectCreate, ProjectList, ProjectDetail, ProjectDelete

urlpatterns = [
    path("", ProjectList.as_view(), name="list_project"),
    path("<int:pk>/", ProjectDetail.as_view(), name="detail_project"),
    path("create/", ProjectCreate.as_view(), name="create_project"),
    path("delete/<int:pk>/", ProjectDelete.as_view(), name="delete_project"),
]
