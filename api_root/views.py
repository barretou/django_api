from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class DrinksList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    
    def get(self, request, format=None):
        drinks = Drink.objects.all().order_by('name')
        serializer = DrinkSerializer(drinks, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)



class DrinksDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Drink.objects.get(pk=pk)
        except Drink.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        drink = self.get_object(pk)
        serializer = DrinkSerializer(drink)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        drink = self.get_object(pk)
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        drink = self.get_object(pk)
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)