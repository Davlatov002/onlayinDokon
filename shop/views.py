from .models import Praduct, Category
from .serialazer import Praductserializers, UpdatePraductserialazer, SearchPraductserializers, CreateCategorySerializers, CategorySerializers, UpdateCategorySerialazer, CreatePraductserializers
from rest_framework.decorators import api_view
from rest_framework import status, serializers
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

from django.db.models import Max

@swagger_auto_schema(method="POST", request_body=CreateCategorySerializers)
@api_view(['POST'])
def category_creat(request):
    if request.method == 'POST':
        category = CreateCategorySerializers(data=request.data)
        if category.is_valid():
            category.save()
            return Response(category.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST) 

@swagger_auto_schema(method='DELETE', operation_description="O'chirmoqchi bo'lgan Categoryni ID sini kirting")
@api_view(['DELETE'])
def category_delet(request, pk):
    if request.method == 'DELETE':
        try:
            category = Category.objects.get(id=pk)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        category.delete()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def categorys(request):
    if request.method == 'GET':
        categorys = Category.objects.all()
        serializer = CategorySerializers(categorys, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def categorys_get_id(request, pk):
    if request.method == 'GET':
        categorys = Category.objects.get(id=pk)
        serializer = CategorySerializers(categorys, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
@swagger_auto_schema(method='PATCH', request_body=UpdateCategorySerialazer, operation_description="Yangilamaoqchi bo'lgan Categoryning ID sini kirting")
@api_view(['PATCH'])
def category_update(request, pk):
    try:
        category = Category.objects.get(id=pk)  
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)      
    data = Praductserializers(instance=category, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def praduct(request):
    if request.method == 'GET':
        praduct = Praduct.objects.all()
        serializer = Praductserializers(praduct, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)  
    
@swagger_auto_schema(method='GET', query_serializer=SearchPraductserializers, operation_description="Mahsulot nomi yoki narxi bo'yicha mahsulotlarni qidirishlari mumkin")
@api_view(['GET'])
def product_search(request):
    if request.method == 'GET':
        praductsearch = request.query_params.get('search')
        try:
            praducts = Praduct.objects.filter(price=praductsearch)
        except:
            praductsearch = str(request.query_params.get('search'))
            praducts = Praduct.objects.filter(name=praductsearch)
        if praducts.exists():
            serializer = Praductserializers(praducts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def praduct_id(request, pk):
    if request.method == 'GET':
        try:
            praducts = Praduct.objects.get(id=pk) 
        except: 
            return Response(status=status.HTTP_400_BAD_REQUEST)      
        serializer = Praductserializers(praducts)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='GET')
@api_view(['GET'])
def praduct_expensive(request):
    if request.method == 'GET':
        try:
            # Eng qimmat mahsulot(lar)ni oling
            max_price = Praduct.objects.aggregate(Max('price'))['price__max']
            praducts = Praduct.objects.filter(price=max_price)
        except Praduct.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        serializer = Praductserializers(praducts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='POST', request_body=CreatePraductserializers, operation_description="Malumotlarni kirting")
@api_view(['POST'])
def praduct_created(request):
    praduct = Praductserializers(data=request.data)
    if praduct.is_valid():
        praduct.save()   
        return Response(praduct.data, status=status.HTTP_201_CREATED)      
    else:                      
        return Response(status=status.HTTP_404_NOT_FOUND)   
    
@swagger_auto_schema(method='PATCH', request_body=UpdatePraductserialazer, operation_description="Yangilamaoqchi bo'lgan pradukniing ID sini kirting")
@api_view(['PATCH'])
def praduct_update(request, pk):
    try:
        praduct = Praduct.objects.get(id=pk)  
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)      
    data = Praductserializers(instance=praduct, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
@swagger_auto_schema(method='DELETE', operation_description="O'chirmoqchi bo'lgan Praducningning ID ni kirting")
@api_view(['DELETE'])
def praduct_delete(request, pk):
    if request.method == 'DELETE':
        try:
            praduct = Praduct.objects.get(id=pk)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        praduct.delete()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)