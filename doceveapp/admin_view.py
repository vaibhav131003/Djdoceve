from django.db import connection
from .import tuple_to_dict
from django.shortcuts import redirect
from django.shortcuts import render
from rest_framework.decorators import api_view
from doceveapp.serializers import TeacherSerializer
from doceveapp.models import Teachers
from django.views.decorators.clickjacking import xframe_options_exempt
from doceveapp.serializers import AdministratorSerializer
from doceveapp.serializers import Administrator

# Create your views here.
@api_view(['GET','POST','DELETE'])
def CategoryInterface(request):
    return render(request,'CategoryInterface.html')

@api_view(['POST','DELETE','GET'])
def LoginPage(reuqest):
    return render(reuqest,"LoginPage.html")

@api_view(['POST','DELETE','GET'])
def AdminLogin(reuqest):
    return render(reuqest,"admin_register.html")

@api_view(['GET','POST','DELETE'])
def CheckAdminLogin(request):
    try:
        if request.method == 'GET':
            q = "select * from  doceveapp_administrator  where emailid='{0}' and password ={1} ".format(request.GET['emailid'],request.GET['password'])

            print(q)
            cursor = connection.cursor()
            cursor.execute(q)
            record = tuple_to_dict.ParseDictSingleRecord(cursor)
            print("check",record)
            # if(len(record)==0):
                
            #     return render(request,"AdminLogin.html",{'message':"Invalid Adminid/Password"})
            # else:
    
            #     print("xxxxxxxxxx",record)
            return render(request,"Login2.html",{'data':record})
    except Exception as e:
        print("Error : ",e)
        return render(request,"forgotpass.html",{'data':[]})
    

@xframe_options_exempt
@api_view(['GET','POST'])
def AdminSubmit(request):
    if request.method == 'POST':
        administrator_serializer = AdministratorSerializer(data=request.data)
        if administrator_serializer.is_valid():
            administrator_serializer.save()
            return render(request,"admin_register.html")
        return render(request,"admin_register.html")