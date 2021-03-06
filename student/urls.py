"""srs2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include,url
from . import views
from django.contrib.auth.decorators import login_required



urlpatterns = [
    url(r'^$',views.home,name='student_home'),
    #url(r'^list_json/$', views.student_list_json.as_view(), name="student_list_json"),
 	url(r'^home/$',views.home_json,name='student_home_json'),
 	url(r'^sbadmin/$',views.home_sbadmin,name='student_home_sbadmin'),
 	url(r'^new/$', views.student_new, name='student_new'),
 	url(r'^(?P<pk>\d+)/remove$', views.student_remove, name='student_remove'),
 	url(r'^(?P<pk>\d+)/edit$', views.student_edit, name='student_edit'),
 	url(r'^(?P<pk>\d+)/$', views.student_detail, name='student_detail'),
 	url(r'^list_json/$', login_required(views.student_list_json.as_view()), name="student_list_json"),
]