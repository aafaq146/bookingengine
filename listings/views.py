from django.shortcuts import render
from rest_framework import viewsets
from . import serializers

from .models import *


# Create your views here.
class Listing_View(viewsets.ModelViewSet):
    serializer_class = serializers.Listing_Serializers
    queryset = Listing.objects.all()
