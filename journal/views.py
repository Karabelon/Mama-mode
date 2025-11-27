from django.shortcuts import render, redirect, get_object_or_404
from .models import JournalEntry
from django.contrib.auth.decorators import login_required

@login_required
def journal(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        if title and content:
            JournalEntry.objects.create(
                user=request.user,
                title=title,
                content=content
            )
            return redirect('journal')

    entries = JournalEntry.objects.filter(user=request.user)
    return render(request, 'journal.html', {"entries": entries})


@login_required
def delete_entry(request, id):
    entry = get_object_or_404(JournalEntry, id=id, user=request.user)
    entry.delete()
    return redirect('journal')




