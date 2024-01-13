from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Basket, Costomer
from .serialazer import BaskerSerialazer, CreateBaskerSerialazer, CostomerSerialazer, CreateCostomerSerialazer, UpdateCostomerSerializer
from rest_framework import status


@swagger_auto_schema(method="POST", request_body=CreateBaskerSerialazer)
@api_view(['POST'])
def basket_add(request):
    if request.method == 'POST':
        basket = CreateBaskerSerialazer(data=request.data)
        if basket.is_valid():
            basket.save()
            return Response(basket.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='DELETE', operation_description="O'chirmoqchi bo'lgan Basket ID sini kirting")
@api_view(['DELETE'])
def basket_delet(request, pk):
    if request.method == 'DELETE':
        try:
            basket = Basket.objects.get(id=pk)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        basket.delete()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method=["GET"])
@api_view(['GET'])
def baskets_get(request):
    if request.method=='GET':
        basket = Basket.objects.all()
        serialazer = BaskerSerialazer(basket, many=True)
        return Response(serialazer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method=["GET"])
@api_view(['GET'])
def baskets_get_id(request, pk):
    if request.method == 'GET':
        baskets = Basket.objects.filter(costomer=pk)
        serializer = BaskerSerialazer(baskets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method="POST", request_body=CreateCostomerSerialazer)
@api_view(['POST'])
def costomer_creat(request):
    if request.method == 'POST':
        costomer = CreateCostomerSerialazer(data=request.data)
        if costomer.is_valid():
            costomer.save()
            return Response(costomer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)  

@swagger_auto_schema(method='DELETE', operation_description="O'chirmoqchi bo'lgan Costomer ID sini kirting")
@api_view(['DELETE'])
def costomer_delet(request, pk):
    if request.method == 'DELETE':
        try:
            praduct = Costomer.objects.get(id=pk)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        praduct.delete()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
@swagger_auto_schema(method='PATCH', request_body=UpdateCostomerSerializer, operation_description="Yangilamaoqchi bo'lgan Costomerning ID sini kirting")
@api_view(['PATCH'])
def costomer_update(request, pk):
    try:
        category = Costomer.objects.get(id=pk)  
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)      
    data = UpdateCostomerSerializer(instance=category, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method=["GET"])
@api_view(['GET'])
def costomer_get(request):
    if request.method=='GET':
        costomers = Costomer.objects.all()
        serialazer = CostomerSerialazer(costomers, many=True)
        return Response(serialazer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

@swagger_auto_schema(method=["GET"])
@api_view(['GET'])
def costomer_get_id(request, pk):
    if request.method=='GET':
        costomer = Costomer.objects.get(id=pk)
        serialazer = CostomerSerialazer(costomer)
        return Response(serialazer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)