from attr import fields
from django import forms

from cursos.models import Course

class InsertCourse(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'description', 'course_slug', 'price', 'image', 'course_banner')

class EditCourse(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'description', 'price', 'image', 'course_banner')