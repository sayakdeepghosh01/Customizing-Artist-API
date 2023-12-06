# artist_api/serializers.py
from rest_framework import serializers
from .models import Artist, Work

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['link', 'work_type']

class ArtistSerializer(serializers.ModelSerializer):
    works = WorkSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ['name', 'user', 'works']
