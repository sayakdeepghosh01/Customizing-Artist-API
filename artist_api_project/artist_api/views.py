from django.shortcuts import render

# Create your views here.
# artist_api/views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
# artist_api/urls.py
from .views import register_user

from django.contrib.auth.models import User
from .models import Artist, Work
from .serializers import ArtistSerializer, WorkSerializer

class WorkListCreateView(generics.ListCreateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [permissions.IsAuthenticated]

class ArtistSearchView(generics.ListAPIView):
    serializer_class = ArtistSerializer

    def get_queryset(self):
        artist_name = self.kwargs['artist_name']
        return Artist.objects.filter(name__icontains=artist_name)

class ArtistWorkListView(generics.ListAPIView):
    serializer_class = WorkSerializer

    def get_queryset(self):
        artist_name = self.kwargs['artist_name']
        try:
            artist = Artist.objects.get(name=artist_name)
            return artist.works.all()
        except Artist.DoesNotExist:
            return Work.objects.none()

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register_user(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        if username and password:
            user = User.objects.create_user(username=username, password=password)
            Token.objects.create(user=user)
            return Response({'message': 'User registered successfully.'})
        else:
            return Response({'message': 'Invalid data provided.'})

