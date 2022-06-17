from pyexpat import model
from django.contrib.auth import authenticate
from re import template
from django.views.generic import TemplateView, ListView, DetailView
from .models import Person, Contact, Product
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


class HomePageView(TemplateView):
    template_name = 'index.html'
    model = Person

class LoginView(TemplateView):
    template_name = 'login.html'
    model = User


class AboutPageView(ListView):
    template_name = 'person_list.html'
    model = Person


class ContactPageView(ListView):
    template_name = 'contact_list.html'
    model = Contact


class ProductPageView(ListView):
    template_name = 'product_list.html'
    model = Product


class ProductView(DetailView):
    template_name = 'product_detail.html'
    model = Product