from rest_framework import serializers
from .models import Message, TypingStatus

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"

class TypingStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypingStatus
        fields = "__all__"
