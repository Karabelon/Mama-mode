from django.shortcuts import render
from .models import BabyActivity

def tracker(request):
    if request.method == "POST":
        activity_type = request.POST["activity_type"]
        time = request.POST["time"]
        notes = request.POST.get("notes", "")

        BabyActivity.objects.create(
            activity_type=activity_type,
            time=time,
            notes=notes
        )

    activities = BabyActivity.objects.order_by("-created_at")

    return render(request, "babytracker.html", {
        "activities": activities
    })








