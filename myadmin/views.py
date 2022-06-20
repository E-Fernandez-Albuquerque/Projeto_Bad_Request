from pyexpat import model
from re import template
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import TemplateView,ListView
from cursos.views import Course
# Create your views here.


class MyAdminHome(TemplateView):
    template_name = 'MyAdminHome.html'


class MyAdminCursos(ListView):
    template_name = 'MyAdminCursos.html'
    model = Course