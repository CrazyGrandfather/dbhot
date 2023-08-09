from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.http import JsonResponse


# Create your views here.

def home(request):
    u1 = reverse('a1', kwargs={'sku_id': '12345dasdasd'})
    print(u1)
    return HttpResponse('这是我们的主页哦')


def login(request):
    return render(request, 'login.html')


def add(request, sku_id):
    print(request.path_info)
    print(sku_id)
    return HttpResponse('这是增加用户接口')


def dele(request):
    name = request.POST.get('name')
    age = request.POST.get('age')

    return JsonResponse({"nameDEL": name, 'ageDEL': age})


def modi(request):
    print(123)
    return redirect("https://www.baidu.com")


def search(request):
    print(123)
    return HttpResponse('这是查询用户接口')
