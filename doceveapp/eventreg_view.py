from django.db import connection
from django.shortcuts import render
from django.shortcuts import redirect
from django.http.response import JsonResponse
from rest_framework.decorators import api_view

from doceveapp.serializers import EventRegistrationSerializer
from doceveapp.models import EventRegistration
from . import tuple_to_dict
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def EventRegistrationInterface(request):
    return render(request,'EventRegistration.html')

@api_view(['GET','POST'])
def EventRegistrationSubmit(request):
    if request.method == 'POST':
        eventregistraion_serializer = EventRegistrationSerializer(data=request.data)
        if eventregistraion_serializer.is_valid():
            eventregistraion_serializer.save()
            return render(request,"EventRegistration.html",{"message":"Record Submitted Successfully"})
        return render(request,"EventRegistration.html",{"message":"Fail to Submit Record"})