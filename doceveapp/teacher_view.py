from django.db import connection
from django.shortcuts import render
from django.shortcuts import redirect
from django.http.response import JsonResponse
from rest_framework.decorators import api_view

from doceveapp.serializers import TeacherSerializer
from doceveapp.models import Teachers
from . import tuple_to_dict
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def TeacherrecInterface(request):
    return render(request,'TeacherrecInterface.html')

@api_view(['GET','POST'])
def TeacherrecSubmit(request):
    if request.method == 'POST':
        teacher_serializer = TeacherSerializer(data=request.data)
        if teacher_serializer.is_valid():
            teacher_serializer.save()
            return render(request,"TeacherrecInterface.html",{"message":"Record Submitted Successfully"})
        return render(request,"TeacherrecInterface.html",{"message":"Fail to Submit Record"})