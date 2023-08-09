"""DJ2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from little_dj import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('home/', views.home),
    path('login/', views.login,name='lg'),
    path('user/', ([
                       path('add/<str:sku_id>', views.add, name="a1"),
                       path('dele/', views.dele),  # /user/dele/
                       path('modi/', views.modi),
                       path('search/', views.search),
                   ], None, None)),
    path('users/', include(([
                                path('add/', views.add, name="s1"),
                                path('dele/', views.dele),  # /user/dele/
                                path('modi/', views.modi),
                                path('search/', views.search),
                            ], None)))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
