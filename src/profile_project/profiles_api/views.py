from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class HelloApiView(APIView):
    """Test API Views."""

    def get(self, reqquest, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
        'Uses HTTP Methods as function (get, post, put, patch, delete)',
        'It is similar to a traditional django view',
        'Gives you the most control over your logic',
        'Is mapped maunally tp URIs '
        ]

        return Response({'message': 'Hello!', 'api_view': an_apiview})
