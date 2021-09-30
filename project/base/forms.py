from django import forms
from rest_framework import serializers
from .models import Image, Analysis

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'image')

class AnalysisForm(forms.ModelForm):
    image = forms.ModelChoiceField(queryset=Image.objects.all())
    class Meta:
        model = Analysis
        fields = ('nome', 'tipo', 'status')
        