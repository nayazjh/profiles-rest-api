from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers
from . import models


# Create your views here.

class HelloApiView(APIView):
    """Test API Views."""

    serializer_class = serializers.HelloSerializer

    def get(self, reqquest, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
        'Uses HTTP Methods as function (get, post, put, patch, delete)',
        'It is similar to a traditional django view',
        'Gives you the most control over your logic',
        'Is mapped maunally tp URIs '
        ]

        return Response({'message': 'Hello!', 'api_view': an_apiview})

    def post(self, request):
        """creates a hello message with a name."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """handles updating an object."""

        return Response ({'method': 'put'})

    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request."""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Deletes an Object."""

        return Response({'method': 'delete'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet."""

    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """Return a hello Message."""

        a_viewset = [
        'Uses Actions (list, create, retrive, update, partial_update)',
        'Automatically maps to URLs using routers',
        'Provides more functionality with less code.'
        ]

        return Response ({'message': 'Hello', 'a_viewset': a_viewset})


    def create(self, request):
        """Create a new hello message."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handles getting an object by its id."""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handles updating an object."""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handles partial update of an object."""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handles removing an object."""

        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and creating updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
