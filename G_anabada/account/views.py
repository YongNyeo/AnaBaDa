# Create your views here.
import logging
from http.client import HTTPResponse

from django.contrib import auth
from django.contrib.auth import authenticate
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from rest_framework.response import Response

from .forms import RegisterForm
from .serializer import Aserializer
from .models import Member
from rest_framework import generics
from rest_framework.views import APIView
from django.shortcuts import render
from .serializer import Aserializer


# def get(self,request):
#     queryset = User1.objects.all()
#     serializer = Aserializer(queryset,many=True)
#     return JsonResponse(serializer.data,safe=False)


class Register(APIView):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        account_id = request.data.get('account_id', "")
        email = request.data.get('email', "")
        nickname = request.data.get('nickname', "")
        name = request.data.get('name', "")
        phone_number = request.data.get('phone_number', "")
        password = request.data.get('password', "")

        if Member.objects.filter(account_id=account_id).exists():
            return render(request, 'idexist.html', {'account_id': account_id})

        Member.objects.create(account_id=account_id, password=password, name=name, email=email, nickname=nickname,
                              phone_number=phone_number)

        return render(request, 'signup_ok.html', {'account_id': account_id})


class Login(APIView):
    def get(self,request):
        return render(request, 'login.html')
    @csrf_exempt
    def post(self,request):
        account_id = request.POST.get('account_id')
        password = request.POST.get('password')
        context = {}
        user = authenticate(request, username=account_id, password=password)


        if user is not None: # 올바른 로그인 정보 입력시.
            request.session['m_id'] = account_id  # 여기서 세션값에 멤버id와 이름이 넘어감
            request.session['m_name'] = request.POST.get('name')

            context['m_id'] = account_id
            context['m_name'] =  request.POST.get('name')
            return render(request, 'main.html', context)

        else:  # 들어온값이 db없으면.

            return render(request, 'login.html', context)


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('home')
    return render(request, 'signup.html')


class MainView(TemplateView):
    template_name = "Base_page.html"
