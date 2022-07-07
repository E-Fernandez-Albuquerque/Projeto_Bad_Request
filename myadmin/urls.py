from django.urls import path
from .views import new_user, edit_user, delete_user, new_lesson, edit_lesson, myadmin_users, MyAdminHome, MyAdminCursos, delete_course, delete_lesson, edit_course, myadmin_lesson, new_course

app_name = 'myadmin'

urlpatterns = [

    #MYADMIN
    path('', MyAdminHome.as_view(), name='adminhome'),

    #CURSOS
    path('cursos/', MyAdminCursos.as_view(), name='admincursos'),
    path('cursos/deletar-curso/<int:id>', delete_course, name='deletar' ),
    path('cursos/editar-curso/<int:id>', edit_course, name='edit'),
    path('cursos/criar-curso/', new_course, name='create'),
    path('cursos/editar-curso/<int:id>/aulas', myadmin_lesson, name='adminaulas'),
    path('cursos/editar-curso/<int:id>/aulas/deletar-aula/<slug:lesson_slug>', delete_lesson, name='deletar-aula'),
    path('cursos/editar-curso/<int:id>/aulas/editar-aula/<slug:lesson_slug>', edit_lesson, name='editar-aula'),
    path('cursos/editar-curso/<int:id>/aulas/criar-aula', new_lesson, name='criar-aula'),

    #USUARIOS
    path('usuarios/', myadmin_users, name='adminusers'),
    path('usuarios/criar-usuario', new_user, name='criar-user'),
    path('usuarios/editar-usuario/<int:id>', edit_user, name='editar-user'),
    path('usuarios/deletar-usuario/<int:id>', delete_user, name='deletar-user')

]