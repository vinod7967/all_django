"""gs115 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from school import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('homefun/', views.homefun, name='homefun'),
    path('homecl/', views.HomeClassView.as_view(), name='homecl'),
    path('aboutfun/', views.aboutfun, name='aboutfun'),
    path('aboutcl/', views.AboutClassView.as_view(), name='aboutcl'),
    path('contactfun/', views.contactfun, name='contactfun'),
    path('contactcl/', views.ContactClassView.as_view(), name='contactcl'),
    # path('newsfun/', views.newsfun, name='newsfun')
    path('newsfun/', views.newsfun, {'template_name':'school/news.html'}, name='newsfun'),
    path('newsfun2/', views.newsfun, {'template_name':'school/news2.html'}, name='newsfun2'),
    # path('newscl/', views.NewsClassView.as_view(), name='newscl')
    path('newscl/', views.NewsClassView.as_view(template_name='school/news.html'), name='newscl'),
    path('newscl2/', views.NewsClassView.as_view(template_name='school/news2.html'), name='newscl2')
]

