from attr import fields
from django import forms

from .models import Course, CoursePosts, LessonPosts

class PostForm(forms.ModelForm):
    class Meta:
        model = CoursePosts
        fields = ('author', 'course', 'text')


class LessonPostForm(forms.ModelForm):
    class Meta:
        model = LessonPosts
        fields = ('author', 'course', 'lesson', 'text')
