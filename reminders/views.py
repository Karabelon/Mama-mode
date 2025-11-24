from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Reminder

def reminders(request):
    google_calendar_url = None

    if request.method == "POST":
        event_name = request.POST["event_name"]
        date = request.POST["date"]
        details = request.POST["details"]

        
        Reminder.objects.create(
            event_name=event_name,
            date=date,
            details=details
        )

        
        formatted_date = date.replace("-", "")
        google_calendar_url = (
            "https://calendar.google.com/calendar/render?"
            f"action=TEMPLATE&text={event_name}"
            f"&dates={formatted_date}/{formatted_date}"
            f"&details={details}"
        )

    reminders = Reminder.objects.order_by("-created_at")

    return render(request, "reminders.html", {
        "google_calendar_url": google_calendar_url,
        "reminders": reminders
    })


