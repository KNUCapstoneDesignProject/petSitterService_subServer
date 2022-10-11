from rest_framework import serializers
from .models import Document, Location

class DocumentSerializer(serializers.ModelSerializer):
    uploadedFile = serializers.FileField(use_url=True)

    class Meta:
        model = Document
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'