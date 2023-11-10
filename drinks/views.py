from django.http import JsonResponse
from .models import Drinks
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# applying all method in single function
@api_view(['GET', 'POST'])
def drink_list(request, format=None):
    if request.method == "GET":
        #get all drinks
        drinks = Drinks.objects.all()
        # serialize the drinks
        serializer = DrinkSerializer(drinks, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        # create a new drink
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data" : serializer.data, "message": "success", "status" : "success"}, status=status.HTTP_201_CREATED)
        return Response({"data" : serializer.errors,"message": "error", "status" : "error"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id, format=None):      # parameters will be passed to this function parameters drinks/id
    try :
        drink = Drinks.objects.get(pk=id)
    except Drinks.DoesNotExist:
        return Response({"message": "error", "status" : "error"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        # get a drink
        serializer = DrinkSerializer(drink)
        return Response({"data" : serializer.data, "message": "success", "status" : "success"}, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data" : serializer.data, "message": "success", "status" : "success"}, status=status.HTTP_200_OK)
        return Response({"data" : serializer.errors,"message": "error", "status" : "error"}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        drink.delete()
        return Response({"message": "success", "status" : "success"}, status=status.HTTP_204_NO_CONTENT) 



# # Create your views here.
# def drink_list(request):
#     #get all drinks
#     drinks = Drinks.objects.all()
#     # serialize the drinks
#     serializer = DrinkSerializer(drinks, many=True)
#     return JsonResponse(serializer.data, safe=False)
