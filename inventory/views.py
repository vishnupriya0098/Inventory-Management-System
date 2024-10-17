from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.core.cache import cache
from .models import Item
from .serializers import ItemSerializer
print(1)
# Create Item
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_item(request):
    print("Token used: ", request.auth)
    print("Received data:", request.data) 
    serializer = ItemSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Read Item with Redis Caching
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_item(request, item_id):
    cache_key = f'item_{item_id}'
    item = cache.get(cache_key)
    print("cache",item)
    if not item:
        item = get_object_or_404(Item, pk=item_id)
        cache.set(cache_key, item, timeout=60*15)  # Cache for 15 minutes
    serializer = ItemSerializer(item)
    return Response(serializer.data)



# Update Item
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    serializer = ItemSerializer(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete Item
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_item(request, item_id):
    print(2)
    item = get_object_or_404(Item, pk=item_id)
    print(item)
    item.delete()
    return Response({"message": "Item deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
