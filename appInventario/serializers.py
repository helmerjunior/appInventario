from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import serializers
from appInventario.models import Evento

class DateTimeLocalTimeField(serializers.DateTimeField):
    def to_native(self, value):
        value = timezone.localtime(value)
        return super(DateTimeLocalTimeField, self).to_native(value)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class EventoSerializer(serializers.HyperlinkedModelSerializer):
    start = DateTimeLocalTimeField
    end = DateTimeLocalTimeField
    class Meta:
        model = Evento
        fields = ('title','start','end','allDay')