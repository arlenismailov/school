from django.shortcuts import render
from .models import Teacher, Events, PhotoEvents
from .serializers import TeacherSerializer, EventsSerializer, PhotoEventsSerializer
from rest_framework import viewsets


class EventsView(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer


class TeacherView(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class PhotoEventsView(viewsets.ModelViewSet):
    queryset = PhotoEvents.objects.all()
    serializer_class = PhotoEventsSerializer