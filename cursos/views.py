from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

#from .models import User
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
#from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Course, CourseLesson, BoughtBy
from .forms import PostForm, LessonPostForm

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin

from django.urls import reverse

from frontend.templates.cursos import *

class CoursesView(ListView):
    model = Course

class CourseDetailView(DetailView):
    model = Course
    slug_field = 'course_slug'
    slug_url_kwarg = 'course_slug' 

    def get_context_data(self, **kwargs):
        user = get_object_or_404(User, username=self.request.user.username)
        bought = BoughtBy.objects.filter(user_id=user.id)
        courses = Course.objects.all()
        this_course = Course.objects.get(course_slug=self.kwargs['course_slug'])
        print(this_course)
        user_courses = []

        for course in bought:
            item = Course.objects.get(pk=course.course_id)
            user_courses.append(item)

        context = super().get_context_data(**kwargs)
        context['user'] = user
        context['courses'] = courses
        if this_course in user_courses:
            context['status'] = True 
        else:
            context['status'] = False
        return context


def course_access(request, course_slug):
        print('EXECUTOU')
        user = User.objects.get(username=request.user.username)
        bought = BoughtBy.objects.filter(user_id=user.id)
        courses = []
        this_course = Course.objects.get(course_slug=course_slug)
        print(user)
        print(bought)
        print(this_course)
        for course in bought:
            item = Course.objects.get(pk=course.course_id)
            courses.append(item)
        if this_course in courses:
            print('True')
            return render(request, 'course_detail.html', {'status': True})



class CourseMuralDetailView(FormMixin, DetailView):
    model = Course
    template_name = 'cursos/course_mural.html'
    form_class = PostForm
    slug_field = 'course_slug'
    slug_url_kwarg = 'course_slug'

    def get_success_url(self):
        return reverse('cursos:course_mural', kwargs=self.kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(CourseMuralDetailView, self).form_valid(form)


class CourseLessonDetailView(FormMixin, DetailView):
    model = CourseLesson
    template_name='cursos/course_lesson.html'
    form_class = LessonPostForm
    slug_field = 'lesson_slug'
    slug_url_kwarg = 'lesson_slug'

    def get_success_url(self):
        return reverse('cursos:course_lesson', kwargs=self.kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(CourseLessonDetailView, self).form_valid(form)


