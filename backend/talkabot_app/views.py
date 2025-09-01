from openai import OpenAI
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from talkabot_app.models import CustomUser, Chat, ChatMessage


# Create your views here.
client = OpenAI()



def createChatTitle(user_message):
    try:
        response = client.chat.completions.create(
            model = "gpt-4o-mini",
            messages = [
                {"role": "assistant", "content": "Give a short, descriptive title for this conversation in not more than 5 words"},
                {"role": "user", "content": user_message},
            ]
        )
        title = response.choices[0].message.content.strip()
    except Exception:
        title = user_message[:50]
    return title



@api_view(['POST'])
def prompt_gpt(request):
    chat_id = request.data.get("chat_id")
    content = request.data.get("content")
    
    if not chat_id:
        return Response({"error": "Chat ID was not provided"}, status=400)
    
    if not content:
        return Response({"error": "There was no prompt inputted"}, status=400)
    
    chat, created = Chat.objects.get_or_create(id=chat_id)
    chat.title = createChatTitle(content)
    chat.save()
    
    chat_message = ChatMessage.objects.create(role="user", chat=chat, content=content)
    
    # get the last 10 chat messages tru the related name "messages"
    chat_messages = chat.messages.order_by("created_at")[:10]
    
    openai_messages = [{"role": message.role, "content": message.content } for message in chat_messages]
    
    # if no assistant message(A.I) is in the chat, means its first prompt 
    if not any(message["role"]=="assistant" for message in openai_messages):
        openai_messages.insert(0, {"role": "assistant", "content": "Hello there"})
        
        
    try:
        response = client.chat.completions.create(
            model = "gpt-4o-mini",
            messages = openai_messages
        )
        openai_reply = response.choices[0].message.content
    except Exception as e:
        return Response({"error": f"An error from Openai {str(e)}"}, status=500)
    
    ChatMessage.objects.create(role="assistant", content=openai_reply, chat=chat)
    return Response({"reply": openai_reply}, status=status.HTTP_201_CREATED)
