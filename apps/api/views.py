from django.shortcuts import render
from .serializer import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

# Create your views here.


from rest_framework import status

@api_view(['POST'])
def add_list(request):
    try:
        serializer = BaseSerailizer(data=request.data)
        
        if serializer.is_valid():
            id = serializer.validated_data.get('name')
            print(id)
            dele = Base2.objects.filter(name = id)
            dele.delete()
            # serializer.save()
            return Response({'res': serializer.data})
        else:
            return Response({
                'status': 400,
                'error': serializer.errors
            },)
    except Exception as e:
        print(e)
    
    
@api_view(['GET','POST'])
def update_or_add_or_delete(request):
    try:
        if request.method == "POST":
            res = BaseSerailizer(data = request.data)
            if res.is_valid():
                res.validated_data.get('id')
                res.save()
                
            return Response({
                "status":200,
                "data":res.data
            })
        elif request.method == "GET":
            res = Base2.objects.all()
            serial = BaseSerailizer(res,many=True).data
            print(serial)
            return Response({
                "status":200,
                "data" : serial
            })

    except Exception as e:
        print(e)
        
        
class ClsBase(APIView):
    
    def get(self,request,id=None,*args, **kwargs):
        if id:
            data  = get_object_or_404(Base2,id = id)
            serial = BaseOne(data)
            return Response({
                'status' : 200,
                'data' : serial.data,
            })
        else:
            data  = Base2.objects.all()
            serial = BaseSerailizer(data,many=True)
            return Response({
                'status':200,
                'data' : serial.data
            })
    
    def post(self,request,*args, **kwargs):
        status = None
        data = None
        
        serail = BaseOne(data=request.data)
        if serail.is_valid():
            data1 = serail.save()
            data = BaseOne(data1).data
            status = 200
        else:
            data = 'error'
            status = 400
        return Response({
            'status' : status,
            'data' : data,
        })
            
    def put(self,request,id,*args, **kwargs):
        base = get_object_or_404(Base2,id = id)
        status = None
        data = None
        serial = BaseSerailizer(base,data = request.data)
        if serial.is_valid():
            data1 = serial.save()
            data = BaseSerailizer(data1).data
            status = 200
        else:               
            status = 400
            data = 'error'
        return Response({
            'status' : status,
            'data' : data,
        })