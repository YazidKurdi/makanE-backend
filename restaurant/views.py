import time

from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView

from .models import FoodCategory,MenuItem
from .serializers import FoodCategorySerializer,MenuItemSerializer

class FoodCategoryList(generics.ListAPIView):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodCategorySerializer

class MenuItemDetail(generics.RetrieveAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    lookup_field = 'slug'


class MenuItemSearch(ListAPIView):

    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    # permission_classes = [IsAuthenticated]
    # pagination_class = StandardResultsSetPagination
    filter_backends = [SearchFilter]
    search_fields = ['name']  # Specify fields to search

    def get(self, request, *args, **kwargs):
        # Introduce a 3-second delay
        time.sleep(1.5)
        return super().get(request, *args, **kwargs)