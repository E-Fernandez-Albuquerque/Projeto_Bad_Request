from django.urls import path
from .views import MyAdminHome, MyAdminCursos

urlpatterns = [
    path('', MyAdminHome.as_view(), name='adminhome'),
    path('cursos/', MyAdminCursos.as_view(), name='admincursos')
]