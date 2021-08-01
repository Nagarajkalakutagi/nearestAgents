from django.shortcuts import render
from rest_framework import viewsets
from agents.models import AgentsData
from agents.serializer import AgentsSerializer
from .add_agents_data import add_data
from rest_framework.response import Response
import pgeocode
import numpy
import numpy as np
from operator import itemgetter


def nearest_agents(zip_code):
    data = AgentsData.objects.all().values_list('id', 'zip_code')
    ls = []
    for i in range(len(data)):
        ls.append(data[i][1])

    code = pgeocode.GeoDistance('US')

    # calculating distance between zipcodes
    dt = code.query_postal_code([zip_code], ls)

    ls2 = []
    for i in range(len(dt)):
        if not numpy.isnan(dt[i]):
            ls2.append((dt[i], data[i][0]))

    # sorting
    sr = sorted(ls2, key=itemgetter(0))
    # print(sr)

    ls4 = []
    for i in range(len(sr[:100])):
        data = AgentsData.objects.get(id=sr[i][1])
        serializer = AgentsSerializer(data)
        ls4.append(serializer.data)

    return ls4


class NewYorkCity(viewsets.ViewSet):
    @staticmethod
    def list(request):
        data = nearest_agents('10001')
        return Response(data)


class Boston(viewsets.ViewSet):
    @staticmethod
    def list(request):
        data = nearest_agents('02108')
        return Response(data)


class LosAngeles(viewsets.ViewSet):
    @staticmethod
    def list(request):
        data = nearest_agents('90001')
        return Response(data)


class Chicago(viewsets.ViewSet):
    @staticmethod
    def list(request):
        data = nearest_agents('60601')
        return Response(data)


class Houston(viewsets.ViewSet):
    @staticmethod
    def list(request):
        data = nearest_agents('77001')
        return Response(data)


class Phoenix(viewsets.ViewSet):
    @staticmethod
    def list(request):
        data = nearest_agents('85001')
        return Response(data)


class SanDiego(viewsets.ViewSet):
    @staticmethod
    def list(request):
        data = nearest_agents('92167')
        return Response(data)


class Dallas(viewsets.ViewSet):
    @staticmethod
    def list(request):
        data = nearest_agents('75201')
        return Response(data)


class SanJose(viewsets.ViewSet):
    @staticmethod
    def list(request):
        data = nearest_agents('95101')
        return Response(data)


class Austin(viewsets.ViewSet):
    @staticmethod
    def list(request):
        data = nearest_agents('78714')
        return Response(data)


class Columbus(viewsets.ViewSet):
    @staticmethod
    def list(request):
        data = nearest_agents('43215')
        return Response(data)


# All Agents Data
class Agents(viewsets.ModelViewSet):
    serializer_class = AgentsSerializer
    queryset = AgentsData.objects.all()


# Push Agents data from CSV to Databases
class PushData(viewsets.ViewSet):
    @staticmethod
    def list(request):
        add_data()
        return Response("Done")