from django.shortcuts import render, get_object_or_404
from .models import FrontEndTeam

# Create your views here.

def frontenddev(request, primarykey):
    Front_Details = get_object_or_404(FrontEndTeam, primarykey=primarykey)
    context = {
        'frontend_info': Front_Details
    }

    return render(request, 'FrontendTeam.html', context)