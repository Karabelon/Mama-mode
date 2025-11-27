from django.shortcuts import render, redirect, get_object_or_404
from .models import BabyActivity
from django.contrib.auth.decorators import login_required

@login_required
def babytracker(request):
    if request.method == "POST":
        activity_type = request.POST.get('activity_type')
        description = request.POST.get('description')

        BabyActivity.objects.create(
            user=request.user,
            activity_type=activity_type,
            description=description
        )
        return redirect("babytracker")

    activities = BabyActivity.objects.filter(user=request.user)
    return render(request, "babytracker.html", {"activities": activities})


@login_required
def delete_activity(request, id):
    activity = get_object_or_404(BabyActivity, id=id, user=request.user)
    activity.delete()
    return redirect("babytracker")









