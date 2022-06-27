from django.urls import path
from . import views

urlpatterns = [
    path('cadastro', views.AccountCreateView.as_view()),
    path('login', views.AccountLoginView.as_view(), name='login'),
    path('logout', views.logout_site, name='logout'),
]