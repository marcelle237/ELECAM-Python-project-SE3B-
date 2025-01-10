import os
from django.conf import settings
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.layers import get_channel_layer
from channels.db import database_sync_to_async
from django.urls import path
from django.contrib.auth.models import User
from django.db import models
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib import admin
from django.urls import include
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, viewsets
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer

# Django setup
settings.configure(
    DEBUG=True,
    SECRET_KEY='my_Only_One',
    ROOT_URLCONF=__name__,
    INSTALLED_APPS=[
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'rest_framework',
        'channels',
        'elecam_app',
    ],
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(os.getcwd(), 'db.sqlite3'),
        }
    },
    ASGI_APPLICATION='elecam.routing.application',
    CHANNEL_LAYERS={
        'default': {
            'BACKEND': 'channels.layers.InMemoryChannelLayer'
        }
    },
    STATIC_URL='/static/',
)

application = get_asgi_application()

# Views
@api_view(['GET'])
def eligibility_conditions(request):
    conditions = [
        "Must be a citizen of Cameroon.",
        "Must be 18 years or older.",
        "Must not be under any voting disqualifications.",
    ]
    return Response({"eligibility_conditions": conditions})

@api_view(['GET'])
def election_statistics(request):
    elections = Election.objects.all()
    serializer = ElectionSerializer(elections, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def polling_stations(request):
    region = request.GET.get('region', None)
    stations = PollingStation.objects.filter(region=region) if region else PollingStation.objects.all()
    serializer = PollingStationSerializer(stations, many=True)
    return Response(serializer.data)

# ChatBot Consumer
class ChatBotConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({"message": "Welcome to ELECAM chatbot! Ask me anything."}))

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message', '').lower()

        if "eligibility" in message:
            response = "To vote, you must be 18 years or older, a citizen of Cameroon, and not under disqualification."
        elif "statistics" in message:
            response = "You can view election statistics by navigating to the statistics section."
        elif "polling station" in message:
            response = "Enter your region or city to find the nearest polling station."
        else:
            response = "I'm not sure about that. Please check our website for more information."

        await self.send(text_data=json.dumps({"response": response}))

# Routing
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter([
        path("ws/chatbot/", ChatBotConsumer.as_asgi()),
    ]),
})

# Admin and URL config
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/eligibility/', eligibility_conditions),
    path('api/statistics/', election_statistics),
    path('api/polling-stations/', polling_stations),
]

# Running the server
if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(["manage.py", "runserver", "0.0.0.0:8000"])
