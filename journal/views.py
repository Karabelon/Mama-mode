from django.shortcuts import render, redirect
from .models import JournalEntry

def journal_page(request):
    if request.method == "POST":
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()

       
        if title or content:
            JournalEntry.objects.create(title=title, content=content)

       
        return redirect('journal')


    entries = JournalEntry.objects.all().order_by('-id') 

    return render(request, "journal.html", {"entries": entries})


