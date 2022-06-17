from django.http import HttpResponse
from django.shortcuts import render
from .serializers import UserSerializer

#from .models import User
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
#from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Username em uso')
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        return HttpResponse('usuário cadastrado')



def login_site(request):
    if request.method=='GET':
        return render(request, 'user_login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('password')

        user = authenticate(username=username, password=senha)

        if user:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse('email ou senha invalidos')


def logout_site(request):
    logout(request)
    return redirect('/')
    

#OK - FUNCIONAL
class AccountLoginView(APIView):
    serializer_class = UserSerializer
    def post(self, request, format=None):

        serializer = self.serializer_class(data=request.data)
        data = request.data

        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return Response({'Sucesso': 'Usuário logado'}, status=status.HTTP_200_OK)
            else:
                return Response({'Not found': 'Usuário não localizado'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'Bad request': 'Erro'}, status=status.HTTP_400_BAD_REQUEST)
#OK - FUNCIONAL


#OK - FUNCIONAL
class AccountCreateView(APIView):
    serializer_class = UserSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get('username')
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            queryset = User.objects.filter(email=email)
            if(queryset.exists()):
                return Response({'Falha': 'Email em uso'}, status=status.HTTP_200_OK)
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                user = authenticate(username=username, password=password)

                if user is not None:
                    if user.is_active:
                        login(request, user)
                return Response({'created', 'Usuário criado com sucesso'}, status=status.HTTP_201_CREATED)
        return Response({'Bad request': 'Dados inválidos'}, status=status.HTTP_400_BAD_REQUEST)