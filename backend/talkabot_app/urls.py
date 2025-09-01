from django.urls import path
from talkabot_app import views


urlpatterns = [
    path("prompt_gpt/", views.prompt_gpt, name="prompt_gpt"),
]