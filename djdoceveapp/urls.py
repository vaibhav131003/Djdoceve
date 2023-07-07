"""djdoceveapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,re_path
from doceveapp import admin_view
from doceveapp import teacher_view
from doceveapp import eventreg_view


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/loginpage/$',admin_view.LoginPage),
    re_path(r'^api/categoryinterface/',admin_view.CategoryInterface),

    ############## adding admin register #############
    re_path(r'^api/adminlogin',admin_view.AdminLogin),
    re_path(r'^api/adminregistersubmit',admin_view.AdminSubmit),
    re_path(r'^api/checkadminlogin',admin_view.CheckAdminLogin),

    ############# teacher details #########
    re_path(r'^api/addteacherrecinterface/$',teacher_view.TeacherrecInterface),
    re_path(r'^api/addteacherrecsubmit',teacher_view.TeacherrecSubmit),

    ############# Event Registration ######
    re_path(r'^api/addeventregistrationinterface/$',eventreg_view.EventRegistrationInterface),
    re_path(r'^api/addeventregistrationsubmit',eventreg_view.EventRegistrationSubmit),



]
