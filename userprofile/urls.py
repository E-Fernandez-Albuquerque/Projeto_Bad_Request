from django.urls import URLPattern, path
from .views import user_profile
app_name='user_profile'

urlpatterns = [
    path('', user_profile, name='profile'),
]