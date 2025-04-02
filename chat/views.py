from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

from .models import Message, TypingStatus
from .serializers import MessageSerializer, TypingStatusSerializer

def home(request):
    return render(request, "index.html")  # Ensure this template exists

class SendMessageView(APIView):
    permission_classes = [IsAuthenticated]  # Require authentication

    def post(self, request):
        receiver_id = request.data.get("receiver_id")
        content = request.data.get("content")

        if not receiver_id or not content:
            return Response({"error": "Receiver ID and content are required."}, status=status.HTTP_400_BAD_REQUEST)

        receiver = get_object_or_404(User, id=receiver_id)

        message = Message.objects.create(
            sender=request.user,
            receiver=receiver,
            content=content
        )

        return Response(
            {"message": "Message sent successfully!", "message_id": message.id},
            status=status.HTTP_201_CREATED
        )

class TypingStatusView(APIView):
    permission_classes = [IsAuthenticated]  # Require authentication

    def post(self, request):
        is_typing = request.data.get("is_typing")

        if is_typing is None:
            return Response({"error": "is_typing field is required."}, status=status.HTTP_400_BAD_REQUEST)

        typing_status, created = TypingStatus.objects.get_or_create(user=request.user)
        typing_status.is_typing = is_typing
        typing_status.save()

        return Response({"status": "Typing status updated."}, status=status.HTTP_200_OK)
