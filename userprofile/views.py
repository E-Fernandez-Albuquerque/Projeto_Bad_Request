from django.shortcuts import render
from cursos.models import BoughtBy, Course
from django.contrib.auth.models import User

# Create your views here.
def user_profile(request):
    user = User.objects.get(username=request.user.username)
    bought = BoughtBy.objects.filter(user_id=user.id)
    courses = []

    for course in bought:
        item = Course.objects.get(pk=course.course_id)
        courses.append(item)
    print(courses)
    print(user)
    print(bought)
    context = {
        'courses': courses
    }
    return render(request, 'userprofile.html', context=context)