from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import render

def home(request):
    return HttpResponse("Hello, welcome to the ELECAM web application!")

# To view the HTML page rendered
def landingPage(request):
    return render(request, 'landingpg.html')

def votesInformation(request):
    return render(request, 'features.html')

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