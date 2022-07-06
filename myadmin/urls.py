from django.urls import path
from .views import new_lesson, MyAdminHome, MyAdminCursos, delete_course, delete_lesson, edit_course, myadmin_lesson, new_course

urlpatterns = [
    path('', MyAdminHome.as_view(), name='adminhome'),
    path('cursos/', MyAdminCursos.as_view(), name='admincursos'),
    path('cursos/deletar-curso/<int:id>', delete_course, name='deletar' ),
    path('cursos/editar-curso/<int:id>', edit_course, name='edit'),
    path('cursos/criar-curso/', new_course, name='create'),
    path('cursos/editar-curso/<int:id>/aulas', myadmin_lesson, name='adminaulas'),
    path('cursos/editar-curso/<int:id>/aulas/deletar-aula/<slug:lesson_slug>', delete_lesson, name='deletar-aula'),
    path('cursos/editar-curso/<int:id>/aulas/criar-aula', new_lesson, name='criar-aula'),

]