from re import template
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.views.generic import TemplateView,ListView
from cursos.views import Course, CourseLesson
from .forms import InsertCourse, EditCourse, InsertLesson
from django.contrib import messages
# Create your views here.


class MyAdminHome(TemplateView):
    template_name = 'MyAdminHome.html'


class MyAdminCursos(ListView):
    template_name = 'MyAdminCursos.html'
    model = Course

def delete_course(request, id):
    course = get_object_or_404(Course, pk=id)
    course.delete()

    messages.info(request, 'Curso deletado')

    return redirect('/myadmin/cursos')

def edit_course(request, id):
    edit = get_object_or_404(Course, pk=id)
    form = EditCourse(instance=edit)

    if(request.method=='POST'):
        form = EditCourse(request.POST, instance=edit)

        if form.is_valid():
            edit.save()
            return redirect('/myadmin/cursos')
        else:
            return render(request, 'MyAdminEditarCursos.html', {'form': form, 'edit': edit})
    else:
        return render(request, 'MyAdminEditarCursos.html', {'form': form, 'edit': edit})

def new_course(request):
    if request.method == 'POST':
        form = InsertCourse(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/myadmin/cursos')
    else:
        form = InsertCourse()
        return render(request, 'MyAdminCriarCurso.html', {'form': form})


def myadmin_lesson(request, id):
    courses = Course.objects.get(id=id)
    lessons = CourseLesson.objects.filter(course=courses)
    print(lessons)
    context = {
        'course_id':courses.id,
        'lessons': lessons
    }
    return render(request, 'MyAdminGerenciarAulas.html', context=context)


def delete_lesson(request, id, lesson_slug):
    courses = Course.objects.get(pk=id)
    lesson = CourseLesson.objects.get(course=courses, lesson_slug=lesson_slug)
    lesson.delete()

    messages.info(request, 'Aula deletada')

    return redirect(f'/myadmin/cursos')


def new_lesson(request, id):
    if request.method == 'POST':
        form = InsertLesson(request.POST)
        form.initial['course_id'] = id
        if form.is_valid():
            form.save()
            return redirect('/myadmin/cursos')
    else:
        form = InsertLesson()
        return render(request, 'MyAdminCriarAula.html', {'form': form, 'course_id': id})