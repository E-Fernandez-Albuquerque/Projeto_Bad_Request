from argparse import Namespace
from django.urls import path
from . import views

app_name = 'main2'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='main'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('contact/', views.ContactPageView.as_view(), name='contact'),
    path('products/', views.ProductPageView.as_view(), name='product'),
    path('products/<slug:slug>', views.ProductView.as_view(), name='product_view'),
    path('login/', views.LoginView.as_view(), name='login')
]