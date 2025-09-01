from rest_framework import serializers
from talkabot_app.models import CustomUser, Chat, ChatMessage


class ChatSerializer(serializers.ModelSerializer):
    class meta:
        model = Chat
        fields = "__all__"
        
        
class ChatMessageSerializer(serializers.ModelSerializer):
    class meta:
        model = ChatMessage
        fields = ["id", "role", "content", "created_at"]