
from rest_framework import serializers
from .models import *

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = ('id', 'title', 'text')
