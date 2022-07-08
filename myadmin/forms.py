from attr import fields
from django import forms
from django.contrib.auth.models import User

from cursos.models import Course, CourseLesson, BoughtBy

class InsertCourse(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'description', 'course_slug', 'price', 'image', 'course_banner')

class EditCourse(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'description', 'price', 'image', 'course_banner')


class InsertLesson(forms.ModelForm):
    class Meta:
        model = CourseLesson
        fields = ('course', 'title', 'description', 'lesson_slug', 'video', 'image')


class EditLesson(forms.ModelForm):
    class Meta:
        model = CourseLesson
        fields = ('title', 'description', 'lesson_slug', 'video', 'image')


class EditUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'is_staff')


class InsertUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'is_staff')

    
class BoughtCourses(forms.ModelForm):
    class Meta:
        model = BoughtBy
        fields = ('course', 'user')