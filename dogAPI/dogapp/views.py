from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from dogapp.models import Dog, Breed
from dogapp.serializers import DogSerializer, BreedSerializer

@csrf_exempt
def api_list(request): 
    if request.method == 'GET':
        apivar = Dog.objects.all()
        serializer = DogSerializer(apivar, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def api_listB(request): 
    if request.method == 'GET':
        apivar = Breed.objects.all()
        serializer = BreedSerializer(apivar, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BreedSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def api_detail(request, pk):
    try:
        dvar = Dog.objects.get(pk=pk)
    except Dog.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DogSerializer(dvar)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DogSerializer(dvar, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        dvar.delete()
        return HttpResponse(status=204)

def api_detailB(request, pk):
    try:
        dvar = Breed.objects.get(pk=pk)
    except Breed.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BreedSerializer(dvar)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BreedSerializer(dvar, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        dvar.delete()
        return HttpResponse(status=204)
