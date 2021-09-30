from django.shortcuts import get_object_or_404, render, redirect
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.conf import settings
from django.urls import reverse_lazy
from django.core import serializers

import json

from django.contrib.auth.views import LoginView

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django import forms
from .forms import AnalysisForm, ImageForm
from .models import Analysis, Image

from base.serializers import ImageSerializer, AnalisysSerializer

## Views da API
## ====================================================================
@api_view(['GET'])
def get_images_api(request):
    if request.method == 'GET': 
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        
        return Response(serializer.data)

@api_view(['POST'])
def create_image_api(request):
    if request.method == 'POST':
        form = ImageForm(request.POST)

        new_image = Image.objects.create(
            title = form.data['title'],
            image = '/images/' + form.data['image']
        )

        new_image.save()

        res = json.loads(serializers.serialize('json', [new_image]))

        return Response(res)

@api_view(['GET'])
def get_image_api(request, pk):
    image = Image.objects.get(id=pk)
    serializer = ImageSerializer(image, many=False)
    
    return Response(serializer.data)

@api_view(['POST'])
def create_analysis_api(request, pk):
    image = Image.objects.get(pk=pk)
    if request.method == 'POST' and image is not None:
        form = AnalysisForm(request.POST)

        status = form.data['status'] == 'true'

        new_analysis = Analysis.objects.create(
            name = form.data['nome'],
            tipo = form.data['tipo'],
            status = status,
            image = image
        )

        new_analysis.save()

        res = json.loads(serializers.serialize('json', [new_analysis]))

        return Response(res)

@api_view(['POST'])
def update_analysis_api(request, pk):
    
    analysis = Analysis.objects.get(pk=pk)

    if request.method == 'POST' and analysis is not None:
        form = AnalysisForm(request.POST, instance=analysis)

        status = form.data['status'] == 'true'

        analysis.name = form.data['nome']
        analysis.tipo = form.data['tipo']
        analysis.status = status
        analysis.save()

        return Response(form.data)

@api_view(['POST'])
def delete_analysis_api(request, pk):
    
    analysis = Analysis.objects.get(pk=pk)

    if request.method == 'POST' and analysis is not None:
        analysis.delete()
        return Response({'menssagem': 'A análise de id: ' + str(pk) + ' foi deletada com sucesso'})

@api_view(['GET'])
def analyses_list_api(request):
    if request.method == 'GET': 
        analysis = Analysis.objects.all()
        serializer = AnalisysSerializer(analysis, many=True)

        return Response(serializer.data)

@api_view(['POST'])
def delete_image_api(request, pk):
    
    image = Image.objects.get(pk=pk)

    if request.method == 'POST' and image is not None:
        image.delete()
        return Response({'menssagem': 'A imagem de id: ' + str(pk) + ' foi deletada com sucesso'})

## Views do site
## ====================================================================
def index(request):
    if request.method == 'GET':
        images = Image.objects.all()
        serialized = ImageSerializer(images, many=True)

        context = {
            'images': serialized.data
        }

        return render(request, 'home.html', context)
    
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'upload.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form})

def get_image(request, pk):
    image = Image.objects.get(pk=pk)
    # serializer = ImageSerializer(image, many=False)

    form = AnalysisForm(request.POST)

    analyses = Analysis.objects.all().filter(image=image)
    analyses_serialized = AnalisysSerializer(analyses, many=True)

    context = {
        'image': image,
        'analyses': analyses_serialized.data,
        'form': form
    }

    return render(request, 'image.html', context)

def create_analysis(request, pk):
    image = Image.objects.get(pk=pk)
    if request.method == 'POST':
        form = AnalysisForm(request.POST)

        status = form.data['status'] == 'true'

        new_analysis = Analysis.objects.create(
            nome = form.data['nome'],
            tipo = form.data['tipo'],
            status = status,
            image = image
        )

        new_analysis.save()

        return redirect('/image/' + str(pk) + '/')
