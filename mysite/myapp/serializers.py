from .models import Teacher, Events, PhotoEvents
from rest_framework import serializers


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'


class PhotoEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoEvents
        fields = '__all__'
