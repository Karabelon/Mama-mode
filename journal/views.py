from django.shortcuts import render
from .models import JournalEntry

def journal_page(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]

        JournalEntry.objects.create(
            title=title,
            content=content
        )

    entries = JournalEntry.objects.order_by("-created_at")

    return render(request, "journal.html", {
        "entries": entries
    })

