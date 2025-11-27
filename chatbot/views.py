from django.shortcuts import render
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Count
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import google.generativeai as genai
from .models import ChatMessage
import json

genai.configure(api_key="AIzaSyCSgiktsISLyqa2qbnep7vktoSxxuH4MvM")

model = genai.GenerativeModel('gemini-2.5-flash')


def chatbot(request):
    return render(request, 'chatbot.html')


def generate_bot_response(message):
    try:
        response = model.generate_content(message)
        return response.text
    except Exception as e:
        print("Gemini error:", e)
        return "There was an issue processing your message."


@csrf_exempt
def send_chat_message(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "")

        bot_reply = generate_bot_response(user_message)

        ChatMessage.objects.create(message=user_message, response=bot_reply)

        return JsonResponse({"success": True, "response": bot_reply})

    return JsonResponse({"success": False, "response": "Invalid request"})



