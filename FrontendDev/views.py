from django.shortcuts import render, get_object_or_404
from .models import FrontEndTeam

# Create your views here.

def frontenddev(request, pk):
    Front_Details = get_object_or_404(FrontEndTeam, pk=pk)
    context = {
        'frontend_info': Front_Details
    }

    return render(request, 'FrontendTeam.html', context)