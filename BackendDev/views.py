from django.shortcuts import render, get_object_or_404
from .models import BackEndTeam

# Create your views here.
def backenddev_details(request, pk):
    BackDetails = get_object_or_404(BackEndTeam,pk = pk)
    Backend_info = {
        'Back_info': BackDetails
    }
    return render(request, 'BackendTeam.html', Backend_info)