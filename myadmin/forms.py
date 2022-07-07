from attr import fields
from django import forms

from cursos.models import Course, CourseLesson

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