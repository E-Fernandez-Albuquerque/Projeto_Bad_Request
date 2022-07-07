from re import template
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.views.generic import TemplateView,ListView
from cursos.views import Course, CourseLesson
from .forms import InsertCourse, EditCourse, InsertLesson, EditLesson, InsertUser, EditUser
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from cursos.models import BoughtBy
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

    return HttpResponseRedirect(reverse('myadmin:adminaulas', kwargs={'id':id}))
    # redirect(f'/myadmin/cursos')


def new_lesson(request, id):
    if request.method == 'POST':
        form = InsertLesson(request.POST)
        course = Course.objects.get(id=id)
        if form.is_valid():
            print(course)
            form.save()
            return HttpResponseRedirect(reverse('myadmin:adminaulas', kwargs={'id':id}))
    else:
        form = InsertLesson()
        return render(request, 'MyAdminCriarAula.html', {'form': form})


def edit_lesson(request, id, lesson_slug):
    course = get_object_or_404(Course, pk=id)
    lesson = CourseLesson.objects.get(course=course, lesson_slug=lesson_slug)
    form = EditLesson(instance=lesson)

    if(request.method=='POST'):
        form = EditLesson(request.POST, instance=lesson)

        if form.is_valid():
            lesson.save()
            return redirect('/myadmin/cursos')
        else:
            return render(request, 'MyAdminEditarAula.html', {'form': form, 'edit': lesson})
    else:
        return render(request, 'MyAdminEditarAula.html', {'form': form, 'edit': lesson})



def myadmin_users(request):
    users = User.objects.all().order_by('username')
    return render(request, 'MyAdminUsuarios.html', {'users': users})


# class MyAdminUsers(ListView):
#     template_name = 'MyAdminUsers.html'
#     model = User


def new_user(request):
    if request.method == 'POST':
        form = InsertUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/myadmin/usuarios')
    else:
        form = InsertUser()
        return render(request, 'MyAdminCriarUsuario.html', {'form': form})


def edit_user(request, id):
    user = get_object_or_404(User, pk=id)
    form = EditUser(instance=user)

    if(request.method=='POST'):
        form = EditUser(request.POST, instance=user)

        if form.is_valid():
            user.password = make_password(user.password)
            user.save()
            return redirect('/myadmin/usuarios')
        else:
            return render(request, 'MyAdminEditarUsuario.html', {'form': form, 'edit': user})
    else:
        return render(request, 'MyAdminEditarUsuario.html', {'form': form, 'edit': user})


def delete_user(request, id):
    user = get_object_or_404(User, pk=id)
    user.delete()

    messages.info(request, 'Usuario deletado')

    return redirect('/myadmin/usuarios')


def user_courses(request, id):
    user = get_object_or_404(User, pk=id)
    bought = BoughtBy.objects.filter(user_id=id)
    courses = []

    for course in bought:
        item = Course.objects.get(pk=course.course_id)
        courses.append(item)
    print(courses)
    print(user)
    print(bought)
    context = {
        'user': user,
        'courses': courses
    }
    return render(request, 'MyAdminUsuarioCursos.html', context=context)