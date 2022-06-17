from django.contrib import admin
from .models import Course, CourseLesson, CoursePosts,LessonPosts

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'course_slug')
    prepopulated_fields = {'course_slug': ("title",)}


@admin.register(CourseLesson)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'title', 'description', 'lesson_slug')
    prepopulated_fields = {'lesson_slug': ("title",)}


@admin.register(CoursePosts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'course', 'text', 'date')


@admin.register(LessonPosts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'course', 'lesson', 'text', 'date')