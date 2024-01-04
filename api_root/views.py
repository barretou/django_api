from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def create_and_list_drinks(request, format=None):
    """
    Get all drinks, serialize them and returns JSON
    """
    if request.method == 'GET':
        drinks = Drink.objects.all()
        drinks_serialized = DrinkSerializer(drinks, many=True)
        return Response(drinks_serialized.data, status = status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def edit_and_delete_drink(request, id, format=None):
    """
    Get, edit or delete an specific drink
    """
    try:     
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'GET':
        drink_serialized = DrinkSerializer(drink)
        return Response(drink_serialized.data, status = status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        drink_serialized = DrinkSerializer(drink, data=request.data)
        if drink_serialized.is_valid():
            drink_serialized.save()
            return Response(drink_serialized.data)
        return Response(drink_serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)