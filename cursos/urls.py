from django.urls import path
from .views import CourseMuralDetailView, CoursesView, CourseDetailView, CourseLessonDetailView

app_name='cursos'

urlpatterns = [
    path('', CoursesView.as_view(), name='course'),
    path('<slug:course_slug>', CourseDetailView.as_view(), name='course_details'),
    path('<slug:course_slug>/mural', CourseMuralDetailView.as_view(), name='course_mural'),
    path('<slug:course_slug>/<slug:lesson_slug>', CourseLessonDetailView.as_view(), name='course_lesson')
]