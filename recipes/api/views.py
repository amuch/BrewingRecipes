from rest_framework import generics
from ..models import Style, Malt, MaltWeight, HopAcid, Hop, HopAddition, Yeast, Recipe
from .serializers import StyleSerializer, MaltSerializer

class StyleListView(generics.ListAPIView):
    queryset = Style.objects.all()
    serializer_class = StyleSerializer

class StyleDetailView(generics.RetrieveAPIView):
    queryset = Style.objects.all()
    serializer_class = StyleSerializer

class MaltListView(generics.ListAPIView):
    queryset = Malt.objects.all()
    serializer_class = MaltSerializer

class MaltDetailView(generics.RetrieveAPIView):
    queryset = Malt.objects.all()
    serializer_class = MaltSerializer
