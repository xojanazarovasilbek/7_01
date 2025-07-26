from django.shortcuts import render
from .models import Ichimliklar
from .serializers import IchimlikSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET',])
def ichimlik_list(request):
    ichimlik = Ichimliklar.objects.all()
    serializer = IchimlikSerializer(ichimlik, many=True)
    res = {
        'data':serializer.data,
        'count':len(ichimlik),
        'status':status.HTTP_200_OK,
    }
    return Response(res)


@api_view(['GET',])
def ichimlik_datail(request, pk):
    ichimlik = Ichimliklar.objects.get(id=pk)
    serializer = IchimlikSerializer(ichimlik)
    res ={
        'data':serializer.data,
        'status':status.HTTP_200_OK,
    }

    return Response(res,)


@api_view(["GET",])
def delete_ichimlik(request, pk):
    try:
        ichimlik = Ichimliklar.objects.get(id=pk)
    except Ichimliklar.DoesNotExist:
        return Response({
            'error': 'element mavjud emas',
            'status': status.HTTP_404_NOT_FOUND
        })
    
    ichimlik.delete()
    res = {
        'xabar': "Mufaqiyatli o'chirildi",
        'status': status.HTTP_200_OK
    }
    return Response(res)

@api_view(['POST',])
def ichimlik_create(request):
    serializer = IchimlikSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': status.HTTP_201_CREATED})
    return Response(status=status.HTTP_400_BAD_REQUEST)
    