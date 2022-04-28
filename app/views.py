from ipaddress import ip_address
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from django.core import serializers
from app.serializers import CardSerializer
from .models import *
import json


def get_ip(request):
    return request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', '')).split(',')[0].strip()


@csrf_exempt
def index(request):
    if request.method == "POST":
        serializer = CardSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save(ip_address=get_ip(request))
        else:
            return JsonResponse({"error": True, "msg": "Please fill all the fields"})
        return JsonResponse(serializer.data)

    cards = Cards.objects.all()
    card = json.loads(serializers.serialize('json', cards))

    params = {'cards': card}
    return render(request, 'index.html', params)


@csrf_exempt
def delete_card(request, id):
    Cards.objects.filter(pk=id).delete()

    return JsonResponse({"success":True})
