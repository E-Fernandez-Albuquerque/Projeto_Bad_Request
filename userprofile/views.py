from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from cursos.models import BoughtBy, Course
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .forms import EditUser
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login

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
        'courses': courses,
        'bought': bought
    }
    return render(request, 'userprofile.html', context=context)



def edit_user(request):
    user = get_object_or_404(User, username=request.user.username)
    form = EditUser(instance=user)

    bought = BoughtBy.objects.filter(user_id=user.id)
    courses = []

    for course in bought:
        item = Course.objects.get(pk=course.course_id)
        courses.append(item)


    if(request.method=='POST'):
        form = EditUser(request.POST, instance=user)

        if form.is_valid():
            if form.cleaned_data["username"]:
                user.username = form.cleaned_data["username"]
            if form.cleaned_data["email"]:
                user.email = form.cleaned_data["email"]
            user.save()

            nuser = User.objects.get(username=user.username)
            nuser = authenticate(username=nuser.username, password=nuser.password)
            if user:
                login(request, nuser)
                return redirect('/perfil')
        else:
            return render(request, 'editUserprofile.html', {'form': form, 'edit': user, 'courses': courses, 'bought': bought})
    else:
        return render(request, 'editUserprofile.html', {'form': form, 'edit': user, 'courses': courses, 'bought': bought})