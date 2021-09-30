from rest_framework import serializers

from .models import Analysis, Image

class ImageSerializer(serializers.ModelSerializer):
    fileExtention = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Image
        fields = ['pk', 'title', 'image', 'fileExtention', 'created_at']

    def get_fileExtention(self, obj):
        name = obj.image.url.split('/')[-1]
        extention = name.split('.')[-1]
        return extention

class AnalisysSerializer(serializers.ModelSerializer):

    class Meta:
        model = Analysis
        fields = '__all__'