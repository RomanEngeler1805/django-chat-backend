from api.models import Chat, ChatMessage
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response


@api_view(["POST"])
def chat(request: Request, id: str) -> Response:
    chat = Chat.collection.get("ca1hnzvWSH8g8Cn1O0rc")
    return Response({"user_message": chat.messages[-1].message})
