from argparse import Namespace
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('old/', include('main.urls', namespace='main')),
    path('user/', include('users.urls')),
    path('chat/', include('chat.urls', namespace='chat')),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('frontend.urls')),
    path('cursos/', include('cursos.urls')),
    path('myadmin/', include('myadmin.urls', namespace='myadmin')),
    path('perfil/', include('userprofile.urls', namespace='profile'))
]

#urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]
