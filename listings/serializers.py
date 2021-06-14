from rest_framework import serializers
from .models import *


class Listing_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = "__all__"
