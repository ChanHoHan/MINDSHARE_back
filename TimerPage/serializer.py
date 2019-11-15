from .models import Timer
from rest_framework import serializers


class TimerSerializer(serializers.ModelSerializer):

    timerOwner = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Timer
        fields = ('pk', 'timerOwner', 'category', 'time', 'is_main_category')