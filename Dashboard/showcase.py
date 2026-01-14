from django.shortcuts import render
from FrontendDev.models import FrontEndTeam

def EmpDashboard(request):
    frontendteam = FrontEndTeam.objects.all()
    context = {
        'Frontend_info': frontendteam
    }
    return render(request, 'index.html', context )