from django.urls import URLPattern, path
from .views import user_profile, edit_user
app_name='user_profile'

urlpatterns = [
    path('', user_profile, name='profile'),
    path('editar', edit_user, name='profileEdit')
]