from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from urllib.parse import urlencode
from .models import Reminder

@login_required
def reminders(request):
    if request.method == "POST":
        event_name = request.POST.get("event_name")
        date_str = request.POST.get("date")        # remains a string
        notes = request.POST.get("notes")

        # Save reminder
        Reminder.objects.create(
            user=request.user,
            event_name=event_name,
            date=date_str,        # Django handles the string
            notes=notes
        )

        # Build Google Calendar link (safe version)
        ymd = date_str.replace("-", "")
        google_calendar_url = (
            "https://calendar.google.com/calendar/render"
            "?action=TEMPLATE"
            f"&text={event_name}"
            f"&details={notes or ''}"
            f"&dates={ymd}/{ymd}"
        )

        reminders_qs = Reminder.objects.filter(user=request.user)
        return render(request, "reminders.html", {
            "reminders": reminders_qs,
            "google_calendar_url": google_calendar_url
        })

    # GET request
    reminders_qs = Reminder.objects.filter(user=request.user)
    return render(request, "reminders.html", {"reminders": reminders_qs})



@login_required
def delete_reminder(request, id):
    r = get_object_or_404(Reminder, id=id, user=request.user)
    if request.method == "POST":
        r.delete()
    return redirect("reminders")



