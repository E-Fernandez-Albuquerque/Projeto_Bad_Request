from email.policy import default
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime

class Course(models.Model):
    title = models.CharField(max_length=255, null=False, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2 ,null=False)
    course_slug = models.SlugField(max_length=255, unique=True, null=False)
    image = models.ImageField(default='null', upload_to = 'frontend/static/images/courseImage')
    course_banner = models.ImageField(default='null', upload_to='frontend/static/images/courseBanner')
    presentationVideo = models.FileField(default='null', upload_to='frontend/static/images/courseVideo')

    def __str__(self):
        return self.title

    def url_correction(self):
        url = str(self.image)
        return url[4:]

    def image_url(self):
        url = str(self.image)
        return url[22:]

    def banner_url(self):
        url = str(self.course_banner)
        return url[22:]

    def video_url_correction(self):
        url = str(self.video)
        return url[4:]

    def get_absolute_url(self):
        return reverse('cursos:course_details', kwargs={'course_slug': self.course_slug})


class CourseLesson(models.Model):
    id = models.IntegerField(primary_key=True)
    course = models.ForeignKey(Course, related_name='lesson', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    lesson_slug = models.SlugField(max_length=255, unique=True, null=False)
    video = models.FileField(default='null', upload_to='frontend/static/video/courseLesson')
    image = models.ImageField(default='null', upload_to='frontend/static/images/courseThumbnail')

    def __str__(self):
        return  f'{self.course} / {self.title}'

    def thumbnail_url(self):
        url = str(self.image)
        return url[22:]

    def video_url(self):
        url = str(self.video)
        return url[22:]

    def get_absolute_url(self):
        return reverse('cursos:course_lesson', kwargs={'course_slug':self.course.course_slug, 'lesson_slug': self.lesson_slug})


class CoursePosts(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, related_name='comment', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='comment', on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.author} - {self.course}'


class LessonPosts(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, related_name='lesson_comment', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='lesson_comment', on_delete=models.CASCADE)
    lesson = models.ForeignKey(CourseLesson, related_name='lesson_comment', on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.author} - {self.course}/{self.lesson}'