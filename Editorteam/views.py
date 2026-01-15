from django.shortcuts import render, get_object_or_404
from .models import EditorTeam

# Create your views here.
def editorteam_details(request, pk):
    Editor_Details = get_object_or_404(EditorTeam, pk=pk)
    context = {
        'Editor_info': Editor_Details
    }

    return render(request, 'EditorTeam.html', context)