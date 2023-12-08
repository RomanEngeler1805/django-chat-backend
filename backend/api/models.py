from enum import auto

from fireo.fields import (
    DateTime,
    IDField,
    ListField,
    NestedModelField,
    TextField,
)
from fireo.models import Model


class ChatMessage(Model):
    sender = TextField()  # user or atla
    message = TextField()
    timestamp = DateTime()


class Chat(Model):
    chat_id = IDField()
    user_id = TextField()
    created_at = DateTime(auto=True)
    messages = ListField(NestedModelField(ChatMessage))
